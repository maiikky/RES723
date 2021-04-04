import socket
import _thread
import time 
import sys, errno

host = '127.0.0.1'
port = 12346

Relay_HOST = ''
Relay_PORT = 4444

light_state = "RED"

def car_handler():
    while True: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            command_id = input('Your command:   ')
            s.sendall(bytes(command_id,'utf-8')) # send messages that are 1/4 or 2/4
            command = command_id.split('/')[0]
            answer = 0 

            if command == '1':
                answer = s.recv(1024)
                message = answer.decode('utf-8')
                print(message)
            elif command == '2':
                answer = s.recv(1024)
                message = answer.decode('utf-8')
                print(message)
                command2 = input("Would you like to go there?   Yes/No:  ")
                s.sendall(bytes(command2,'utf-8'))
                if command2 == 'Yes': 
                    location = s.recv(1024)
                    message2 = location.decode('utf-8')
                    print(message2)
            s.close()

def state_handler():
    global light_state
    command = '3/4'
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                s.sendall(bytes(command,'utf-8'))
                light_state = s.recv(1024).decode('utf-8')
                #print(light_state)
                s.close()
        except IOError as e:
            if e.errno == errno.EPIPE:
                print(e.errno)
        time.sleep(1)

def Transfer(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as FirstCarSocket:
        try: 
            FirstCarSocket.bind((Relay_HOST, Relay_PORT))
        except socket.error as e: 
            print(str(e))
        print("Car socket is listening for client in the line")
        FirstCarSocket.listen(1)
        while True: 
            car, address = FirstCarSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            data = car.recv(1024).decode('utf-8')
            if len(data) != 0:
                print(light_state)
                car.sendall(bytes(light_state,'utf-8'))
            car.close()

        
if __name__ == "__main__":
    _thread.start_new_thread(state_handler, ())
    _thread.start_new_thread(Transfer, ())
    _thread.start_new_thread(car_handler, ())
    while True:
        time.sleep(10)


            
