import socket 
import random 
import datetime 
import _thread
import numpy as np 
import statistics as stat
import time 
host = '192.168.1.154'
port = 40000 

print("commands available: \n 1) PUSH\n 2) GET\n 3) NONE")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Provide the information about available parking spot////  t
def cars_motion():
    global mess, parking_spot_availables, car_id
                        #### Determination of the car trajectory inside the network ####
    car_id = 1
    routes = [1,2,3,4]
    exit_routes = [1,2,3,4]
    car_arrival_route = random.choice(routes) # The provenance of the car is chosen randomly
    exit_routes.remove(car_arrival_route) # the different exit possible for the car 
    car_exit_route = random.choice(exit_routes) # the car's exit
    

                        #### Determination of the realtime delay accused ####
    delay = 10 # expressed in minutes 
    sigma = 3
    realtime_delay = int(stat.mean(np.random.normal(delay, sigma, 10))) # the car collects information on the delay of others cars
     
    
                        #### Determination of the parking spot ####
    spots = [1,2,3,4,5,6,7,8,9]
    parking_spot_availables = random.choice(spots)

                        #### Final message to be sent ####
    mess = [car_arrival_route,realtime_delay,car_exit_route,parking_spot_availables,car_id]#this tuple represents the message that will be sent to the access point.
    return mess 

while True: 
    command = input("Enter your command: ")
    if command == 'NONE':
        # Sends exit request to the server
        s.send(command.encode())
        break
    elif command == 'PUSH': 
        s.send(str(command).encode())
        infor = cars_motion()
        s.send(str(infor).encode())
        break
    elif command == 'GET':
        s.send(str(command).encode()) # sends the command GET
        info = cars_motion()
        s.send(str(info).encode()) # send the relevant information for car push, stored under the variable mess

        #s.send(command.encode())
        
    else: 
    	s.send(command.encode())
    reply = s.recv(2048)
    print(reply.decode('utf-8'))

s.close()
