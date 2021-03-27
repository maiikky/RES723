import socket
import _thread
import cars 
import sys
sys.path.append(".")
from AccessPoint import AccessPoint


HOST = ''
PORT = 12346


def con_handler(connection):
    #hello_message = print('Welcome! Your suscription allows you to choose from the following options: \n1) Traffic information\n2) Parking Information')
    #.sendall(bytes(hello_message,"utf-8"))
    message = connection.recv(1024)
    command = message.decode('utf-8')
    result = 0 
    answer = 0 
    
    if  command == '1':
        result = red_light.traffic_information()
    
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

    


    connection.sendall(str.encode(str(result))) 
if __name__ == "__main__":
    global AccessPoint
    red_light = AccessPoint()
    while True: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SystemSideSocket:
            try: 
                SystemSideSocket.bind((HOST, PORT))
            except socket.error as e: 
                print(e)
            print('Car Socket is listenning..')
            SystemSideSocket.listen(1)
            while True: 
                client, address = SystemSideSocket.accept()
                print('Connected to: ' + address[0] + ':' + str(address[1]))
                _thread.start_new_thread(con_handler, (client, ))
            SystemSideSocket.close()