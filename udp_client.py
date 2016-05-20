from socket import *
import sys
import requests
import time

host = "localhost" # This is the ip address of the server to which you are sending your packets. Can be "localhost"
port = 21567 # This is the port number on which the server is listening
buf = 1024 # This is the max size (in bytes) of the packets you are sending
addr = (host,port)

UDPSock = socket(AF_INET,SOCK_DGRAM) # Open a UDP socket


while True: # This is where you repeatedly collect data from the user and send it to the server
    r=requests.get("http://localhost:8000/votes/1")
    data = str(r.json()) # Get your data
    UDPSock.sendto(data,addr) # Set the data to the server
    if data[0] == 'q': # If the data starts with 'q', we are done
        break
    time.sleep(3)
