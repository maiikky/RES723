import sys
sys.path.append(".")
import socket 
import _thread
import statistics as stat
import numpy as np 
import random 
import datetime
import time 

host = ''
port = 40000

CONDITION = [True]

def client_handler(connection): 
    client_id = 0
    answer = 0 
    data = connection.recv(1024)
    message = data.decode('utf-8')
    ''' Message is sent  by client side and must contain: 
          - client_id to reference with register (the list)
          - action: info or parking; 1 being requesting traffic info from server and 2 requesting parking inside a airport garage'''
    request = message.split('/')
    client_id = request[0]
    action = request[1]
    if client_id in register: 
        if action ==  'info': 
            pass 
        elif action == 'parking':
            answer = parking_handler()
    else: 
        print("Client not authorised.")
        connection.close()
        return
    connection.sendall(str(answer).encode())




'''def GET():
    
          ### AGGREGATION OF THE CAR DELAY ###
    mean_delay = 10
    sigma = 3

    car_delay = int(car_get[4])
    lane_delay  = 0
    print(car_get)
    print(len(car_get))
    if mean_delay < car_delay < mean_delay+sigma:
    lane_delay  = [int(car_get[13]),car_delay]
    
    elif mean_delay - sigma < car_delay < mean_delay:
    lane_delay  = [int(car_get[13]),car_delay] 

    elif car_delay < mean_delay - sigma:
    lane_delay = []

    else: 
    lane_delay = []
    print(type(lane_delay))
    return lane_delay'''

def parking_handler(): #This function parsed the information received by cars
    available_spot = 104
    #connection.sendall(str(available_spot.encode())
    return available_spot

def information_handler(Args):
    print(Args)
    print(type(Args))
    return(Args)
    

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

if __name__ == '__main__':
    global register, information, parking
    register = ['4','5']
    #registrer is a list that will implemented somewhere in this code.

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ServerSideSocket:
        try: 
            ServerSideSocket.bind((host, port))
        except socket.error as e: 
            ServerSideSocket.close()
        print('Socket is listenning..')
        ServerSideSocket.listen(1)
        while CONDITION[0]: 
            Client, address = ServerSideSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            _thread.start_new_thread(client_handler, (Client, ))

 
    


    


