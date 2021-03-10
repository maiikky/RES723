import socket 

host = ''
port = 40000

def PROCESSING_SERVERSIDE():
	
			### AGGREGATION OF THE CAR DELAY ###
	mean_delay = 10
	sigma = 3

	car_delay = int(data[4])
	lane_delay  = 0
	if mean_delay < car_delay < mean_delay+sigma:
		lane_delay  = [data[13],car_delay]

	if mean_delay - sigma < car_delay < mean_delay:
		lane_delay  = [data[13],car_delay] 

	if car_delay < mean_delay - sigma:
		lane_delay = 'Not applicable'

	if car_delay >  mean_delay + sigma: 
		lane_delay = 'Not applicable'
	return lane_delay

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host, port)) #if it doesn't work remove one pair of parenthesis
	s.listen(1) #xallows one connection at the time 
	conn, addr = s.accept()
	with conn:
		print("Connected by: ", addr)
		while True:
			data = conn.recv(1024)
			data = data.decode('utf-8')
			print(data)
			print(data[1])
			print(type(data[1]))
			ans = PROCESSING_SERVERSIDE()
			
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


