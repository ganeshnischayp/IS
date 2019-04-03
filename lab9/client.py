# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 5252		

# connect to the server on local computer 
s.connect(('192.168.43.75', port)) 
#10.53.124.251
# receive data from the server 

s.send('503023'.encode()) 
# close the connection 
s.close()



    