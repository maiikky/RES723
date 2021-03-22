import socket
import _thread
import cars 
import access_point

HOST = ''
PORT = 12346

host = '127.0.0.1' 
port = 12345


def con_handler():
    data = connection.recv(1024)
    command = input('Your choice? ') #
    connection.send(bytes(command), "utf-8")


def update_traffic_light(): 
    while True: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host,port))




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ClientSideSocket:
    try: 
        ClientSideSocket.bind((host, port))
    except socket.error as e: 
        ClientSideSocket.close()
        print('Car Socket is listenning..')
        ClientSideSocket.listen(3)
    while True: 
        client, address = ClientSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        _thread.start_new_thread(con_handler, (client, ))