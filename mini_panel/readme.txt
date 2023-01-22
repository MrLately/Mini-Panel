Mini-Panel
Mini Panel is a server control panel for servers hosted on www.serverpoint.com, with minimal functionality. It can log you in, get server status and stats, and also perform actions such as turning on and off, rebooting, and updating.

To use the script, first run pip3 install -r requirements.txt or pip install requests to install the necessary dependencies.

Next, add your email and password in the credentials.txt file with your email on the first line and password on the second line.

Run the script with python server_control.py and it will show the status of your servers right away and refresh every 30 seconds. After any action button is pressed, the script will run the get status function for an immediate refresh.

The script now allows for the selection of multiple servers, and the instance selection dropdown allows the user to select and control any server in the list.

Enjoy!
