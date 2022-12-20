import requests
import json
import headers_data

# Set the email and password for your account
with open("credentials.txt", 'r') as f:
    email = f.readline().strip()
    password = f.readline().strip()

headers_data = headers_data.headers

# Set the API endpoint and the payload
url = 'https://api-v1.serverpoint.com/authenticate'
payload = {'key1': 'value1', 'key2': 'value2'}

# Send the POST request to the API endpoint with the payload
response = requests.post(url, json=payload, headers=headers_data)

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # If the request was successful, parse the response JSON to extract the server_id and access_token
    data = response.json()
    token = data['token']  
    username = data['username']  
    user_level = data['user_level']  
    inactivity_period_minutes = data['inactivity_period_minutes']  
    status = data['status']  
    
    # Store the values in a dictionary
    credentials = {
        'access_token': token,
        'server_id': username,
        'user_level': user_level,
        'inactivity_period_minutes': inactivity_period_minutes,
        'status': status
    }
    
    # Write the dictionary to a file as a JSON object
    with open("credentials.json", 'w') as f:
        import json
        f.write(json.dumps(credentials))
        
else:
    # If the request was not successful, print the status code and the response content
    print(f'Request failed with status code {response.status_code}')
    print(response.content)






