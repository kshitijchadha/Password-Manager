import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import pymysql
from cryptography.fernet import Fernet

# Load encryption key
with open("encryption_key.key", "rb") as key_file:
    KEY = key_file.read()
cipher_suite = Fernet(KEY)

# Database connection
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",  
        password="krakkd123",  
        database="passwordmanager"
    )

# Add a password
def add_password(service, username, password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO passwords (service, username, password) VALUES (%s, %s, %s)",
        (service, username, encrypted_password)
    )
    db.commit()
    db.close()
    messagebox.showinfo("Success", "Password added successfully!")

# Retrieve a password
def retrieve_password(service, master_password):
    if master_password != "krakkd123":
        messagebox.showerror("Error", "Invalid master password!")
        return
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE service = %s", (service,))
    result = cursor.fetchone()
    db.close()
    if result:
        username, encrypted_password = result
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        messagebox.showinfo("Password Retrieved", f"Service: {service}\nUsername: {username}\nPassword: {decrypted_password}")
    else:
        messagebox.showerror("Error", "No password found for the specified service.")

# Delete a password
def delete_password(service):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM passwords WHERE service = %s", (service,))
    db.commit()
    rows_deleted = cursor.rowcount
    db.close()
    if rows_deleted > 0:
        messagebox.showinfo("Success", f"Password for '{service}' deleted successfully!")
    else:
        messagebox.showerror("Error", f"No password found for the service '{service}'.")

# Password Generator
def generate_password():
    length = password_length.get()
    include_upper = upper_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if length < 4 or length > 32:
        messagebox.showerror("Error", "Password length must be between 4 and 32.")
        return

    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    update_strength(password)

# Password Strength Checker
def update_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    strength_bar["value"] = strength * 25
    if strength == 1:
        strength_label.config(text="Weak", fg="red")
    elif strength == 2:
        strength_label.config(text="Fair", fg="orange")
    elif strength == 3:
        strength_label.config(text="Good", fg="blue")
    elif strength == 4:
        strength_label.config(text="Strong", fg="green")
    else:
        strength_label.config(text="Very Weak", fg="red")

# Show/Hide Password Toggle
def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_button.config(text="Hide")
    else:
        password_entry.config(show='*')
        toggle_button.config(text="Show")

# GUI Setup
root = tk.Tk()
root.title("Password Manager")

# Variables
password_length = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

# Add Password Section
tk.Label(root, text="Service").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Username").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=5)

service_entry = tk.Entry(root, width=30)
service_entry.grid(row=0, column=1, padx=10, pady=5)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

toggle_button = tk.Button(root, text="Show", command=toggle_password)
toggle_button.grid(row=2, column=2, padx=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, column=2, padx=10, pady=5)

tk.Button(root, text="Add Password", command=lambda: add_password(
    service_entry.get(), username_entry.get(), password_entry.get())).grid(row=4, column=1, pady=10)

# Retrieve Password Section
tk.Label(root, text="Retrieve Service").grid(row=5, column=0, padx=10, pady=5)
service_retrieve_entry = tk.Entry(root, width=30)
service_retrieve_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Master Password").grid(row=6, column=0, padx=10, pady=5)
master_password_entry = tk.Entry(root, width=30, show="*")
master_password_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Button(root, text="Retrieve Password", command=lambda: retrieve_password(
    service_retrieve_entry.get(), master_password_entry.get())).grid(row=7, column=1, pady=10)

# Delete Password Section
tk.Label(root, text="Delete Service").grid(row=8, column=0, padx=10, pady=5)
service_delete_entry = tk.Entry(root, width=30)
service_delete_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Button(root, text="Delete Password", command=lambda: delete_password(
    service_delete_entry.get())).grid(row=9, column=1, pady=10)

# Password Generator Options
tk.Label(root, text="Password Generator Options").grid(row=10, column=0, columnspan=3, pady=10)
tk.Label(root, text="Length").grid(row=11, column=0, padx=10, pady=5)
tk.Spinbox(root, from_=4, to_=32, textvariable=password_length, width=10).grid(row=11, column=1, pady=5)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).grid(row=12, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=13, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=14, column=0, columnspan=2, sticky="w")

# Password Strength Bar
tk.Label(root, text="Password Strength").grid(row=15, column=0, padx=10, pady=5)
strength_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
strength_bar.grid(row=15, column=1, padx=10, pady=5)

strength_label = tk.Label(root, text="Very Weak", fg="red")
strength_label.grid(row=15, column=2, padx=10, pady=5)

root.mainloop()
