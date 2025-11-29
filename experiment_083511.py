import socket 
from threading import Thread 
from cryptography.fernet import Fernet


s = socket.socket()
print('socket created')
s.bind(("localhost", 9993))
s.listen(3)


def accepting():
    while True:
        c, addr = s.accept()
        print("connected with", addr)
        a = Thread(target = sending,args = (c,addr))
        r = Thread(target = recieve,args = (c,addr))
        a.start()
        r.start()
def sending(c,addr):
	key = Fernet.generate_key()
	c.send(key)
	print("key is sent_s",key)
        
def recieve(c,addr):
	c_key= c.recv(1024)
	print("key recieved_s",c_key)
        

acc = Thread(target = accepting)
acc.start()