import socket 
import time 
import _thread 
import sys, errno

HOST1 = '127.0.0.1'
PORT1 = 4444
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST1, PORT1))
        command = 'Hello'
        s.sendall(bytes(command,'utf-8'))
        message = s.recv(1024).decode('utf-8')
        print(message)
        s.close()
except IOError as e:
    print("error")



    


