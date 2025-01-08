from cryptography.fernet import Fernet

# Generate and save a secure encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'encryption_key.key'.")

if __name__ == "__main__":
    generate_key()

