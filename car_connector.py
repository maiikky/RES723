
import socket
import _thread
import time 

host = '127.0.0.1'
port = 12346

while True:  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((host, port))
            #intro_message = s.recv(1024) #hello_message from server is received here
        command = input('Enter a number')
        s.sendall(bytes(command,'utf-8')) # send messages that are 1 or 2 
        answer = s.recv(1024)
        message = answer.decode()
        print(message)
