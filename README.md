# Password Manager

A simple command-line-based password manager that allows users to securely store, retrieve, update, and delete passwords. The passwords are encrypted using a master encryption key and stored in a MySQL database.

## Features

- **Add Password**: Securely add passwords for different services.
- **Retrieve Password**: Retrieve encrypted passwords for a service and decrypt them using a master password.
- **Update Password**: Update the stored password for a service.
- **Delete Password**: Remove a stored password from the database.
- **Encryption and Decryption**: All passwords are encrypted before being stored, and decryption is only possible with the correct master password.

## Technologies Used

- **Python**: The primary programming language for the application.
- **MySQL**: A relational database to store encrypted passwords.
- **Cryptography**: Used to encrypt and decrypt passwords securely.
- **PyMySQL**: Python library for interacting with MySQL databases.

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python libraries (can be installed via `pip`)

## Installation

1. **Clone the Repository**  
   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
