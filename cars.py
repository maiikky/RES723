# this is the code for the car and its main fucntionality will be generating traffic information: 
# cars' delay have to be modelled (normal distribution, uniform, or exponential)
#
import random 
import datetime 
import _thread
import numpy as np 
import statistics as stat 
import socket 
import time 


host = '192.168.1.154'
port = 40000

condition = [True]

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
    realtime_delay = stat.mean(np.random.normal(delay, sigma, 10)) # the car collects information on the delay of others cars
     
    
                        #### Determination of the parking spot ####
    spots = [1,2,3,4,5,6,7,8,9,10,15,25,50]
    parking_spot_availables = random.choice(spots)

                        #### Final message to be sent ####
    mess = [car_arrival_route, realtime_delay, car_exit_route, parking_spot_availables,car_id]#this tuple represents the message that will be sent to the access point.

    

class cars: 
    def __init__(self):
        _thread.start_new_thread(cars_motion, ())  
    def get_value(self): 
        return mess
    class CAM(): 
        def header(self): 
            version = 1.1
            mess_id = 2
            pass 
        def body(self): 
            pass 
        def position_reference(self): 
            pass

   
# the message that should be send to the access point should be organised as a tuple. 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host,port))
        except socket.error as e:   
            print(str(e))
        while condition[0]:
            cars_motion()
            mess_1 = str(mess)
            s.sendall(mess_1.encode())
            print('OK')
            rep = s.recv(2048)
            
            print(rep.decode())
        #s.close()
#we need to insert a time sleep inside the while loop