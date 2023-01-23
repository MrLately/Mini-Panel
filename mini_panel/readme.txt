Mini-Panel
Mini Panel is a server control panel for servers hosted on www.serverpoint.com, with minimal functionality. It allows you to login, get server status and stats, and perform actions such as turning on and off, rebooting, and updating.

To use the script, first run pip3 install -r requirements.txt or pip install requests to install the necessary dependencies.

Run the script with python run.py. It will check for a credentials.txt file, if it doesn't exist it will open a Tkinter login window for you to enter your email and password. Once you press login, the window will close, credentials.txt will be created, and server_control.py will run.

The script now allows for the selection of multiple servers, and the instance selection dropdown allows the user to select and control any server in the list.

Enjoy!
