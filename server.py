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
global available_spot, parking_spot 




def light_state_update(): 



def client_handler(connection): 
    client_id = 0
    answer = 0 
    while CONDITION[0]:
        data = connection.recv(1024)
        message = data.decode('utf-8')
        ''' Message is sent  by client side and must contain: 
            - client_id to reference with register (the list)
            - action: info or parking; 1 being requesting traffic info from server and 2 requesting parking inside a airport garage'''
        request = message.split('/')
        client_id = request[0]
        action = request[1]
        if client_id in register: 
            if action ==  'information': 
                answer = information_handler() 
            elif action == 'parking':
                answer = parking_handler()
            
        else: 
            print("Client not authorised.")
            connection.close()
            return
        connection.sendall(str(answer).encode())

def parking_handler(): #This function parsed the information received by cars

    available_spot = [100,90,45,60,50,40,30,20,10,1]
    available_spot = random.choice(available_spot) - 1

    available_locations = ['A','B','C']
    available_locations = random.choice(available_locations)
    options = 'Parking '+available_locations+' has '+str(available_spot) + ' spots available'
    return options


def information_handler():
    
    treatment =  cars_motion()
    return(treatment)
    

def cars_motion():
    global lane_speed 
                        #### Determination of the car trajectory inside the network ####
    
    routes = [1,2,3,4]
    exit_routes = [1,2,3,4]
    car_arrival_route = random.choice(routes) # The provenance of the car is chosen randomly
    exit_routes.remove(car_arrival_route) # the different exit possible for the car 
    #car_exit_route = random.choice(exit_routes) # the car's exit
    

                        #### Determination of the realtime delay accused ####
    delay = 5 # expressed in minutes 
    sigma = 2
    realtime_delay1 = int(stat.mean(np.random.normal(delay, sigma, 5))) # the car collects information on the delay of others cars
    realtime_delay2 = int(stat.mean(np.random.normal(delay, sigma, 5))) 
    realtime_delay3 = int(stat.mean(np.random.normal(delay, sigma, 5)))

                        #### Determination of the distance mapped to each lane
    options = [100, 150, 230, 280, 300, 340, 370, 400, 420, 500]
    distances = []
    for _ in exit_routes: # underscore ask python not to save in place in the memory while operating the for loop
        ans = random.choice(options)
        distances.append(ans)
                        #### Computation of the "lane speed" #### based on v = d/t
    lane_speed = [(realtime_delay1 * distances[0]), (realtime_delay2 * distances[1]), (realtime_delay3 * distances[2])]
    # possible to return the lane speed with the smallest weight    
    return lane_speed 

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

 
    


    


