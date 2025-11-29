import socket 
from threading import Thread
import os 
import time

s= socket.socket()
print("socket created")
s.bind(("100.69.45.231",9999))
s.listen(3)
print("waiting for connections...")
c,addr = s.accept()
print("coonected to ",addr)
count = 0
root_dir = '.'  # Start from the current directory
for dir_path, dir_names, file_names in os.walk(root_dir):
    print(f"Directory: {dir_path}")
    dirpath = "Directory "+dir_path+"\n"
    dir = dirpath.encode()
    c.sendall(dir)
    for dir_name in dir_names:
        print(f"  Subdirectory: {dir_name}")
        dirname = "    Subdirectory "+dir_name+"\n"
        dir_naam = dirname.encode()
        c.sendall(dir_naam)
    for file_name in file_names:
        print(f"  File: {file_name}")
        filename = "    File "+file_name+"\n"
        file = filename.encode()
        c.sendall(file)
        count+=1
        print(count)
print("succesfully transmitted")
