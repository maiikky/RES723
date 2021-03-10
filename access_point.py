# This file is the access-point of our network. It has the followong functionality: 
# 1--> establishes sockets communication with the cars
# 2--> for each car connected it requests an update (contains the information about the traffic)
# 3--> organise the information received, identify  which cars need it and transmit the information 
# we will implement UDP instead of TCP as n the context of a traffic jam the amount of cars trying to communicate will create severe congestion 
# on the network. 

import socket
import cars as cars 

CONDITION = [True] # we assume that a proximity sensors is dedecting a car at the red light

host = ''
port = 40000

## SOCKET CREATION ##
def GET():
	reply = str(123)
	print("Nice automation dude!")
	return reply

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port)) #if it doesn't work remove one pair of parenthesis
    s.listen(5) # allows one connection at the time 
    while CONDITION[0]:
        conn, addr = s.accept()
        with conn:
            print("Connected by: ", addr)  
            data = conn.recv(1024)
            data = data.decode('utf-8')
            dataMessage = data.split(' ', 1) #i might not need this bit
            command = dataMessage[0]
            if command ==  'Launch':
                reply = GET()
                
            elif command == 'EXIT':
                print("Connection to client interrupted.")
            
            elif command == 'KILL': 
                print("Our server is shutting down.")
                s.close()
                break 
            else: 
                print( "Unknown command.")
            conn.sendall(reply.encode())	


# i can have this array: ['get',store] that represents the commands that are 
# going to be used. Get will send the new parameters to the cars and stored 
# save the cars parameters in the memory and will be available at the next get. 
