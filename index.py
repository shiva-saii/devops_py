import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to validate password
def is_valid_password(password):
    return len(password) >= 6

# Function to handle registration
def register_user():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # Check if email is valid
    if not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email address.")
        return
    
    # Check if password is valid
    if not is_valid_password(password):
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    # Save user information to a file
    with open('users.txt', 'a') as file:
        file.write(f"{username},{email},{password}\n")
    
    messagebox.showinfo("Success", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the widgets
tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
