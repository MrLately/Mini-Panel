# Mini-Panel
Mini Panel is a server control panel for www.serverpoint.com servers
with minimal functionality. It can log you in, get server status and
stats. It can also perform a few actions such as turn on and off,
reboot, and update.

pip3 install -r requirements.txt
or pip install requests, so far its all it uses.

put email on first line of credentials.txt
put password on the second line of credentials.txt

run server_control.py

It will show status right away and refresh every 30 seconds. After
any action button is pressed, it will run get status for an
immidiate refresh.

At this point it only works with one server because
I only have one. If anyone would like to add that
ability feel free. I'd love to see it get better in
the wild.

enjoy!
