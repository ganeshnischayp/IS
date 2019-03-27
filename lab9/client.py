# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12346				

# connect to the server on local computer 
s.connect(('10.53.90.164', port)) 
#10.53.124.251
# receive data from the server 

s.send('Thank you for connecting'.encode()) 
# close the connection 
s.close()



    