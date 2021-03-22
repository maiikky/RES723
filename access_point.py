
import _thread 
import statistics as stat
import numpy as np 
import random 
import datetime
import time 
global traffic_light, lane_speed

def loop():

                #### State of the traffic light ####
    states = ["RED","GREEN","ORANGE"]
    while True: 
        traffic_light = states[0]
        #insert a send message here indicating -90 seconds to green light
        time.sleep(90)
        traffic_light = states[1]
        #insert a send message here indicating -30 seconds to orange light
        time.sleep(30)
        traffic_light = states[2]
        #insert a send message here indicating -10 seconds to RED light
        time.sleep(10)

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
    for _ in exit_routes: # underscore ask python not to save in place in the memory while operating the for loop
        ans = random.choice(options)
        distances.append(ans)
                        #### Computation of the "lane speed" #### based on v = d/t
    lane_speed = [(realtime_delay1 * distances[0]), (realtime_delay2 * distances[1]), (realtime_delay3 * distances[2])]
    # possible to return the lane speed with the smallest weight    
    return lane_speed,traffic_light


class access_point:
    def __init__(self): 
        _thread.start_new_thread(loop, ())
        self.state = "RED"

        def run(self):
            while True: 
                self.update_state()
                time.sleep(10)

        _thread.start_new_thread(run, (self,))
        
    def get_name(self): 
        return "access point"
        
    def update_state(self):
        if traffic_light == states[0]:
            self.state = "RED"
        elif traffic_light == "GREEN":
            self.state = "GREEN"
        elif traffic_light == "ORANGE":
            self.state = "ORANGE"
         
    def get_state():
        self.update_state()
        return self.state


        
    