# Save as server.py
# Message Receiver
import os
from socket import *
import struct
import serial.tools.list_ports
import time



print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)
ser = None

for p in ports:
    print(p[1])
    if "Arduino" in p[1]:
        ser = serial.Serial(port=p[0])

if ser == None:
    print("No Arduino Device was found connected to the computer")
    exit(0)


host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
while True:
  (data, addr) = UDPSock.recvfrom(buf)
  #data = data.encode(encoding='UTF-8')
  #print("Received message: " + data)
  c = float(str(data)[2:-1])
  print(c)
  if c<= -150:
    ser.write(('B%s' % 45).encode('utf-8'))
    print(('B%s' % 45).encode('utf-8'))
    time.sleep(5)
    ser.write((str(1)).encode('utf-8'))
    time.sleep(1)
    ser.write((str(2)).encode('utf-8'))
    time.sleep(1)
    break
UDPSock.close()
os._exit(0)