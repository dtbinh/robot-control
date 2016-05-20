# This code will run on the robot

from gopigo import *
from socket import *
import sys

host = "localhost" #This is the robot's IP address. If you are testing locally, it can be "localhost"
port = 21567 # This is the port where the robot is listening
buf = 1024 # This is the max size (in bytes) of the udp packets
addr = (host,port)

UDPSock = socket(AF_INET,SOCK_DGRAM) # Create the socket
UDPSock.bind(addr) # Bind the ip address and port number to the socket

while True: 
    data,addr = UDPSock.recvfrom(buf) # Receive data from the socket - this call waits until some data is received
    print data
    if data[0] == 'q':
        break
    
