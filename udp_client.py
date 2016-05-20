from socket import *
import sys
import requests
import time
bypass = requests.Session()
bypass.trust_env = False

host = "localhost" # This is the ip address of the server to which you are sending your packets. Can be "localhost"
port = 21567 # This is the port number on which the server is listening
buf = 1024 # This is the max size (in bytes) of the packets you are sending
addr = (host,port)

UDPSock = socket(AF_INET,SOCK_DGRAM) # Open a UDP socket


while True: # This is where you repeatedly collect data from the user and send it to the server
    s=bypass.post('http://192.168.1.6:8000/sessions/', data={'num_votes':0})
    print s.status_code
    data =s.json()
    session_id = data['id']
    time.sleep(5)
    r=bypass.get("http://192.168.1.6:8000/votes/"+str(session_id))
    votes=r.json()
    s=bypass.put('http://192.168.1.6:8000/sessions/'+str(session_id)+'/', data={'num_votes':len(votes)})
    data = votes # Get your data
    string_data=''
    for vote in votes:
        string_data += vote['vote']
    print session_id, string_data
    UDPSock.sendto(string_data,addr) # Set the data to the server
    #if string_data[0] == 'q': # If the data starts with 'q', we are done
    #    break
