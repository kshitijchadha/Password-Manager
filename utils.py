import bcrypt
import pyperclip

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def copy_to_clipboard(data):
    pyperclip.copy(data)
    print("Data copied to clipboard!")
