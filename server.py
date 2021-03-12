import socket 

host = ''
port = 40000

def GET(information):
	
			### AGGREGATION OF THE CAR DELAY ###
	mean_delay = 10
	sigma = 3

	car_delay = int(car_get[4])
	lane_delay  = 0
	if mean_delay < car_delay < mean_delay+sigma:
		lane_delay  = [car_get[13],car_delay]

	if mean_delay - sigma < car_delay < mean_delay:
		lane_delay  = [car_get[13],car_delay] 

	if car_delay < mean_delay - sigma:
		lane_delay = 'Not applicable'

	if car_delay >  mean_delay + sigma: 
		lane_delay = 'Not applicable'
	return lane_delay

def PUSH(message): #This function parsed the information received by cars
	x = (-len(message))+1
	message_ = message[x:-1] # message without the brackets, easier to split with delimiter ','
	print(message_)
	return x
	#car_id = 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port)) 
    s.listen(1) # allows one connection at the time 
    conn, addr = s.accept()
    with conn:
        print("Connected by: ", addr)
        while True:
            command = conn.recv(1024)
            command = command.decode('utf-8')
            if command == 'PUSH':
                car_push = conn.recv(1024)
                car_push = car_push.decode('utf-8')
                ans = PUSH(car_push)

            if command == 'GET':	
                car_get = conn.recv(1024)
                car_get = car_get.decode('utf-8')
                ans = GET(car_get)
			
			
			
			#dataMessage = data.split(' ', 1)
			#command = dataMessage[0]
			#if command ==  'GET':
			#	reply = GET()
				
			#elif command == 'EXIT':
			#	print("Connection to client interrupted.")
			
			#elif command == 'KILL': 
			#	print("Our server is shutting down.")
			#	s.close()
			#	break 
			#else: 
			#	print( "Unknown command.")
            conn.sendall(str(ans).encode())	


