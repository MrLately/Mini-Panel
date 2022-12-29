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

At this point it only shows multiple servers but can only control
first in the list. I will make a function to work with the
instance selection dropdown unless anyone else would like to show
me how its done. I'd love to see it get better in
the wild.

enjoy!
![example](https://user-images.githubusercontent.com/94589563/208738741-ddace90d-815f-4ab7-88fc-01da94b8f291.png)
![eample2](https://user-images.githubusercontent.com/94589563/208738804-a9892f1f-84dd-47c5-839a-4ca6e5dda39a.png)
![example3](https://user-images.githubusercontent.com/94589563/208738813-455b9019-796b-484e-ac56-61a19ef6e033.png)
![example4](https://user-images.githubusercontent.com/94589563/208738825-afca2d51-e7db-4f4a-ab68-a50107b8689b.png)
![example5](https://user-images.githubusercontent.com/94589563/208738835-e0dd5f50-3afc-4116-9165-f5d3fef892f1.png)
![q](https://user-images.githubusercontent.com/94589563/209963542-79d1259b-69aa-40aa-bd33-b510b18069e1.png)
