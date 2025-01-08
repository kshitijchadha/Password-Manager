# Password Manager

A simple password manager built using Python, Tkinter for the GUI, and MySQL for storing encrypted passwords.

## Features

- **Add a password**: Save encrypted passwords to a MySQL database.
- **Retrieve a password**: Decrypt and view stored passwords.
- **Delete a password**: Remove a password entry from the database.
- **Password Generator**: Generate random secure passwords.
- **Password Strength Checker**: Evaluate the strength of generated passwords.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/kshitijchadha/Password-Manager.git
    cd Password-Manager
    ```

2. Create a `.env` file in the project directory with the following content (replace with your own credentials):
    ```plaintext
    DB_PASSWORD=your_mysql_password
    MASTER_PASSWORD=your_master_password
    ```

3. Create the MySQL database and table:
    ```sql
    CREATE DATABASE passwordmanager;
    USE passwordmanager;
    CREATE TABLE passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        service VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password BLOB NOT NULL
    );
    ```

4. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python app.py
    ```

## Usage

- **Add a password**: Enter the service name, username, and password, then click "Add Password".
- **Retrieve a password**: Enter the service name and master password to retrieve the stored password.
- **Delete a password**: Enter the service name and click "Delete Password".
- **Generate a password**: Use the password generator to create a random password and customize it based on length and character types.

## Security

- The application uses encryption to securely store passwords in the database.
- The master password is used to decrypt the stored passwords.

