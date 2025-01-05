import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="password",  # Replace with your MySQL password
            database="PasswordManager"
        )
        print("Connected to MySQL Database!")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Credentials (
            id INT AUTO_INCREMENT PRIMARY KEY,
            site_name VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password TEXT NOT NULL
        );
        """)
        connection.close()
        print("Database table ensured.")

