import socket 
 

host = '127.0.0.1'
port = 40000 

CONDITION = [True]

print("commands available: \n 1) parking\n 2) information\n 3) NONE")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while CONDITION[0]:
    c_id = '4' 
    command = input("Enter your command: ")
    if command == 'NONE':
        message = command
        s.send(message.encode())
    elif command == 'parking': 
        message = str(c_id)+'/'+command
        s.send(message.encode())
    elif command == 'information':
        message = str(c_id)+'/'+command
        s.send(message.encode()) # send the relevant information for car push, stored under the variable mess  
    elif command == 'light'
        message =    
    else: 
    	s.send(command.encode())
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

s.close()

