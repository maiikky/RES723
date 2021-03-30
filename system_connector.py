import socket
import _thread
import cars 
import sys
sys.path.append(".")
from AccessPoint import AccessPoint
from cars import Cars 


HOST = ''
PORT = 12346

def con_handler(connection):
    data = connection.recv(1024)
    message = data.decode('utf-8')
    path = message.split('/')
    command = path[0]   
    id = path[1]
    result = 0 
    answer = 0 

    if id in user_id.get_susbriber():
        if  command == '1':
            result = red_light.traffic_information()
            connection.sendall(str.encode(str(result)))
        elif command == '2':
            result = red_light.get_parking()
            connection.sendall(str.encode(str(result))) 
            message = connection.recv(1024)
            answer = message.decode()
            if answer == 'Yes':
                result = red_light.get_specificPlace()
                connection.sendall(str.encode(str(result)))
            else: 
                connection.close()
        elif command == '3':
            result = red_light.get_state()
            print(result)
            connection.sendall(str.encode(str(result)))
    else: 
        result = 'Not authorised'
        connection.sendall(bytes(result, 'utf-8'))
    connection.close()
     
if __name__ == "__main__":
    global red_light
    global user_id
    red_light = AccessPoint()
    user_id = Cars()
    while True: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SystemSideSocket:
            try: 
                SystemSideSocket.bind((HOST, PORT))
            except socket.error as e: 
                print(e)
            print('System Socket is listenning..')
            SystemSideSocket.listen(1)
            while True: 
                client, address = SystemSideSocket.accept()
                print('Connected to: ' + address[0] + ':' + str(address[1]))
                _thread.start_new_thread(con_handler, (client, ))
            SystemSideSocket.close()