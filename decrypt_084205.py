import os
from cryptography.fernet import Fernet

# Get a list of encrypted files
files = []
for file in os.listdir():
    if os.path.isfile(file) and file not in ["encrypt.py", "decrypt.py", "thekey.key"]:
        files.append(file)

# Load the encryption key
with open("thekey.key", "rb") as key_file:
    secretkey = key_file.read()

# Decrypt files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    
    try:
        decrypted_contents = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
        print(f"Decrypted: {file}")
    except:
        print(f"Error: {file} could not be decrypted. It might not have been encrypted or has been modified.")

print("Decryption complete!")

