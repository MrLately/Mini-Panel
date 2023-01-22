import tkinter as tk
import requests
import json
import subprocess
import os
import headers_data
from tkinter import StringVar

headers_data = headers_data.headers

os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

root = tk.Tk()
root.title("Mini Panel 4 SP")
screen_width = root.winfo_screenwidth()
message_label = tk.Label(root, text="")

   
def get_server_status():
    # Read the credentials.json file
    with open("credentials.json", 'r') as f:
        data = json.loads(f.read())

    # Make the GET request to the server status endpoint
    response = requests.get('https://api-v1.serverpoint.com/vs/status', headers=headers_data)
    
    # Extract the server status from the response
    server_status = response.json()
    vs_instance_status = server_status["vs_instance_status"]
    instance_id = []
    messages = []
    for instance in vs_instance_status:
        # Add the instance ID to the list of instance IDs
        instance_id.append(instance["id"])

        # Create a message for this instance
        message = "Instance ID: {}\nStatus: {}\nOS: {}\nOS Class: {}\nOS Family: {}\nOS Name: {}\nOS Subname: {}\nDate Deployment Ordered: {}\nDate Deployment Completed: {}\nOS Updates Available: {}\nOS Updates Status: {}\nIs Deployed: {}".format(
            instance["id"],
            instance["status"],
            instance["os"],
            instance["os_class"],
            instance["os_family"],
            instance["os_name"],
            instance["os_subname"],
            instance["date_deployment_ordered"],
            instance["date_deployment_completed"],
            instance["os_updates_available"],
            instance["os_updates_status"],
            instance["is_deployed"]
        )
        messages.append(message)
    
    # Update the message label with the messages for all instances
    message_label.config(text="\n\n".join(messages))
    
    # Update the credentials dictionary with the list of instance IDs
    credentials["instance_id"] = instance_id

# Write the updated data back to the file
    with open("credentials.json", "w") as f:
        json.dump(credentials, f)
        f.flush()
    
    # Call the function again after 30 seconds
    root.after(30000, get_server_status)
    
# Read the JSON object from the file
try:
    with open("credentials.json", 'r') as f:
        credentials = json.loads(f.read())
       
except FileNotFoundError:
    subprocess.run(['python', 'server_login.py'])
    # code to read the credentials from the file created by server_login.py
    with open("credentials.json", 'r') as f:
        credentials = json.loads(f.read())
    get_server_status()


try:
    with open("credentials.json", 'r') as f:
        credentials = json.loads(f.read())
        selected_instance_value = credentials.get("selected_instance", credentials["instance_id"][0])
except FileNotFoundError:
    selected_instance_value = credentials["instance_id"][0]

# create a variable to store the selected instance
selected_instance = StringVar(root)

# set the initial value of the variable to the first instance ID in the credentials dictionary or the selected_instance value
selected_instance.set(selected_instance_value)

# create the option menu widget
instance_dropdown = tk.OptionMenu(root, selected_instance, *credentials["instance_id"])

# update the credentials dictionary with the selected instance when the user makes a selection
def update_instance(*args):
    credentials["selected_instance"] = selected_instance.get()
    # write the updated data back to the file
    with open("credentials.json", "w") as f:
        json.dump(credentials, f)
        f.flush()

# bind the trace event to the update_instance function
selected_instance.trace("w", update_instance)

# pack the dropdown menu to display it in the GUI
instance_dropdown.pack()

     
def get_server_stats():
    # Read the credentials.json file
    with open("credentials.json", "w") as f:
        json.dump(credentials, f)
        f.flush()

    # Make the GET request to the server statistics endpoint
    response = requests.get(f'https://api-v1.serverpoint.com/vs/instance/{credentials["selected_instance"]}/stats', headers=headers_data)

    
    # Extract the server statistics from the response
    server_stats = response.json()["vs_resource_statistics"][0]
    disk_usage = server_stats["disk_usage_current"][0]
    data_transfer = server_stats["data_transfer_current"][0]
    ram_usage = server_stats["ram_usage_every_hour"]
    
    # Create a message with the server statistics information
    message = "Disk usage: {} GB / {} GB\nData transfer (24Hr): {} GB in / {} GB out\nData transfer (30 Days): {} GB in / {} GB out".format(
        disk_usage["disk_used_gb"],
        disk_usage["disk_size_gb"],
        data_transfer["last_day_incoming_gb"],
        data_transfer["last_day_outgoing_gb"],
        data_transfer["last_month_incoming_gb"],
        data_transfer["last_month_outgoing_gb"],
    )
    message += "\nRAM usage (last 24 hours):"
    for hour in ram_usage:
        message += f"\n  Hour {hour['hour']}: {hour['ram_usage_percentage']}%"
       
    # Update the message label with the server statistics message
    message_label.config(text=message)  
      
# code to use the credentials
def send_request(selected_instance, access_token, action):
    url = f"https://api-v1.serverpoint.com/vs/instance/{selected_instance}/actions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    payload = {"action": action}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        get_server_status()
    else:
        message_label.config(text=f"Failed to {action} server")

def turn_on_server(selected_instance, access_token):
    send_request(selected_instance, access_token, "on")
    
def turn_off_server(selected_instance, access_token):
    send_request(selected_instance, access_token, "off")

def reboot_server(selected_instance, access_token):
    send_request(selected_instance, access_token, "reboot")

def update_server(selected_instance, access_token):
    send_request(selected_instance, access_token, "installupdates")
   
message_label = tk.Label(root, text="")
message_label.pack(side='bottom')

status_button = tk.Button(root, text="Server Stats", command=get_server_stats)
status_button.pack(side='left')

stats_button = tk.Button(root, text="Get Status", command=get_server_status)
stats_button.pack(side='left', after=status_button)

on_button = tk.Button(root, text="Turn On", command=lambda: turn_on_server(credentials["selected_instance"], credentials["access_token"]))
on_button.pack(side='left')

off_button = tk.Button(root, text="Turn Off", command=lambda: turn_off_server(credentials["selected_instance"], credentials["access_token"]))
off_button.pack(side='left', after=on_button)

reboot_button = tk.Button(root, text="Reboot", command=lambda: reboot_server(credentials["selected_instance"], credentials["access_token"]))
reboot_button.pack(side='left', after=off_button)

update_button = tk.Button(root, text="Update", command=lambda: update_server(credentials["selected_instance"], credentials["access_token"]))
update_button.pack(side='left', after=reboot_button)

get_server_status()

root.mainloop()




