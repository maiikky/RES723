#from access_point import access_point
import socket 
import time 
import _thread 


def connection_handler(): 
    print("Commands available: \n 1) Light \n 2) Lane information\n 3) Parking")
    command = input('Enter a number')















"""'if __name__ == '__main__':
    global access_point
    access = acces_point()
    register = ['4','5']
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
            _thread.start_new_thread(connection_handler, (Client, ))"""
