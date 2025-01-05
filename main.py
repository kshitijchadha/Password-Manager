from database import connect_to_database, create_table
from utils import hash_password, copy_to_clipboard

def menu():
    connection = connect_to_database()
    if not connection:
        return

    while True:
        print("\nPassword Manager")
        print("1. Add Credential")
        print("2. Retrieve Credential")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            site_name = input("Enter site name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            # Call database function to add credential
        elif choice == "2":
            site_name = input("Enter site name to search: ")
            # Call database function to retrieve credential
        elif choice == "3":
            connection.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
