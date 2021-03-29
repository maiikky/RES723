import socket 
import time 
import _thread 

HOST1 = '127.0.0.1'
PORT1 = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST1, PORT1))
command = 'This message notifies a connection'
s.sendall(bytes(command,'utf-8'))
information = s.recv(1024)
message = information.decode()
print(message)
s.close()




    


