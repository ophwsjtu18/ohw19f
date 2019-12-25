# Save as client.py
# Message Sender
import os, json, time
from socket import *
host = "172.18.4.33" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)


while True:
    while True:
        print('detecting')
        time.sleep(2)
        with open('objects.json', 'r') as f:
            data = json.loads(f.read())
            if 'person' in data:
                shifted_x = data['person'][0]['center_x'] - 320
		print(shifted_x)
                break
    #shifted_x = shifted_x.encode(encoding='UTF-8')
    UDPSock.sendto(str(shifted_x), addr)
    if shifted_x == b'exit':
        break
UDPSock.close()
os._exit(0)
