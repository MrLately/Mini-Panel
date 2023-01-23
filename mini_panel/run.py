import tkinter as tk
from tkinter import simpledialog
import subprocess
import os

if not os.path.exists("credentials.txt"):
    # Create a Tkinter window for the user to enter their email and password
    root = tk.Tk()
    root.withdraw()

    email = simpledialog.askstring("Login", "Enter your email:", parent=root)
    password = simpledialog.askstring("Login", "Enter your password:", parent=root, show='*')

    # Close the Tkinter window
    root.destroy()

    # Write the email and password to a file
    with open("credentials.txt", 'w') as f:
        f.write(email + '\n')
        f.write(password)
    
subprocess.run(["python", "server_control.py"])
