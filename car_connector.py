
import socket
import _thread
import time 

host = '127.0.0.1'
port = 12346

Relay_HOST = ''
Relay_PORT = 4444

def car_handler(s):
    while True:  
        answer = 0 
        
        if command == '1':
            answer = s.recv(1024)
            message = answer.decode()
            print(message)
        elif command == '2':
            answer = s.recv(1024)
            message = answer.decode()
            print(message)
            command2 = input("Would you like to go there?   Yes/No:  ")
            s.sendall(bytes(command2,'utf-8'))
            if command2 == 'Yes': 
                location = s.recv(1024)
                message2 = location.decode()
                print(message2)
                s.close()
            else: 
                s.close()
        elif command == '3': 
            answer = s.recv(1024)
            message = answer.decode()
            print(message)
        s.close()

def state_handler(s):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        command = '3/4'
        global light_state
        while True: 
            s.sendall(bytes(command,'utf-8'))
            reply = s.recv(1024)
            light_state = reply.decode()
            time.sleep(5)
        

        
        


def Transfer(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as FirstCarSocket:
        try: 
            FirstCarSocket.bind((Relay_HOST, Relay_PORT))
        except socket.error as e: 
            print(str(e))
        print("Car socket is listening for client in the line")
        FirstCarSocket.listen(1)
        while True: 
            CAR, address = FirstCarSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            data = FirstCarSocket.recv(1024)
            if data: 
                print(light_state)
                FirstCarSocket.sendall(bytes(light_state,'utf-8'))
                return
        FirstCarSocket.close()

        
if __name__ == "__main__":
    while True: 
        _thread.start_new_thread(state_handler, ())
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            command = input('Your command:   ')
            s.sendall(bytes(command,'utf-8')) # send messages that are 1 or 2 
            _thread.start_new_thread(car_handler, (s,))
            _thread.start_new_thread(Transfer, ())


            
