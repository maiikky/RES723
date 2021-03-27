
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
        answer = 0 
        #location = 0 
        s.sendall(bytes(command,'utf-8')) # send messages that are 1 or 2 
        if command == '1':
            answer = s.recv(1024)
            message = answer.decode()
            print(message)
        elif command == '2':
            answer = s.recv(1024)
            message = answer.decode()
            print(message)
            command2 = input("Would you like to go there?   Yes/No:  ")
            s.sendall(bytes(command2,'utf-8'))
            if command2 == 'Yes': 
                location = s.recv(1024)
                message2 = location.decode()
                print(message2)
                s.close()
            else: 
                s.close()


        
       
        s.close()

        
        #answer = s.recv(1024)
        #message = answer.decode()
        #print(message)

