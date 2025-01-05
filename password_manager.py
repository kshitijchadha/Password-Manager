import mysql.connector
import pymysql
from cryptography.fernet import Fernet
import getpass

# Load the encryption key
with open("encryption_key.key", "rb") as key_file:
    KEY = key_file.read()
cipher_suite = Fernet(KEY)

# Database connection
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",  
        password="krakkd123",  # This is your database password (master password)
        database="passwordmanager"
    )

# Add a password
def add_password(service, username, password):
    encrypted_password = cipher_suite.encrypt(password.encode())  # Encrypt the password
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO passwords (service, username, password) VALUES (%s, %s, %s)",
        (service, username, encrypted_password)
    )
    db.commit()
    db.close()
    print("Password added successfully!")

# Retrieve a password
def get_password(service):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE service = %s", (service,))
    result = cursor.fetchone()
    db.close()
    if result:
        username, encrypted_password = result
        decrypt_choice = input("Do you want to decrypt the password? (y/yes to decrypt): ").lower()
        if decrypt_choice in ["y", "yes"]:
            master_password = getpass.getpass("Enter your master password: ")
            # Check if the master password is correct (same as the database password)
            if master_password == "krakkd123":  # Check against your actual database password (master password)
                decrypted_password = cipher_suite.decrypt(encrypted_password).decode()  # Decrypt the password
                print(f"Service: {service}")
                print(f"Username: {username}")
                print(f"Password: {decrypted_password}")
            else:
                print("Incorrect master password. Decryption failed.")
        else:
            print("Password decryption skipped.")
    else:
        print("No password found for the specified service.")

# Update a password
def update_password(service, new_password):
    encrypted_password = cipher_suite.encrypt(new_password.encode())  # Encrypt the new password
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE passwords SET password = %s WHERE service = %s",
        (encrypted_password, service)
    )
    db.commit()
    db.close()
    print("Password updated successfully!")

# Delete a password
def delete_password(service):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM passwords WHERE service = %s", (service,))
    db.commit()
    db.close()
    print("Password deleted successfully!")

# Menu-driven CLI
def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            add_password(service, username, password)

        elif choice == "2":
            service = input("Enter the service name: ")
            get_password(service)

        elif choice == "3":
            service = input("Enter the service name: ")
            new_password = getpass.getpass("Enter the new password: ")
            update_password(service, new_password)

        elif choice == "4":
            service = input("Enter the service name: ")
            delete_password(service)

        elif choice == "5":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
