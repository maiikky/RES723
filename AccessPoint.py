
import _thread 
import statistics as stat
import numpy as np 
import random 
import datetime
import time 

def parking(): 
    global options 
    available_spot = [100,90,45,60,50,40,30,20,10,1]
    available_spot = random.choice(available_spot) - 1

    available_locations = ['A','B','C']
    available_locations = random.choice(available_locations)
    options = 'Parking '+available_locations+' has '+str(available_spot) + ' spots available'

def traffic_light(): 
    global states, light
    states = ["RED","GREEN","ORANGE"]
    while True: 
        light = states[0]
        time.sleep(90)
        light = states[1]
        time.sleep(30)
        light = states[2]
        time.sleep(10)
    return light

def loop():

    global lane_speed
                #### Cars motion simulation ####
                
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
    for i in exit_routes: # underscore ask python not to save in place in the memory while operating the for loop
        ans = random.choice(options)
        distances.append(ans)
                        #### Computation of the "lane speed" #### based on v = d/t
    lane_speed = [(realtime_delay1 * distances[0]), (realtime_delay2 * distances[1]), (realtime_delay3 * distances[2])]
    # possible to return the lane speed with the smallest weight    
    return lane_speed,traffic_light


class AccessPoint:
    def __init__(self): 
        _thread.start_new_thread(loop, ())
        _thread.start_new_thread(parking, ())
        _thread.start_new_thread(traffic_light, ())
        self.state = "RED"
        self.parking_info = 0

        def run(self):
            while True: 
                self.update_state()
                time.sleep(10)

        _thread.start_new_thread(run, (self,))
        
    def get_name(self): 
        return "access point A"
        
    def update_state(self):
        if light == states[0]:
            self.state = "RED"
        elif light == "GREEN":
            self.state = "GREEN"
        elif light == "ORANGE":
            self.state = "ORANGE"
         
    def get_state(self):
        self.update_state()
        return self.state

    def get_parking(self): 
        self.parking_info = options
        return self.parking_info 

    def traffic_information(self):
        self.delay_info = lane_speed
        return self.delay_info 


        
    