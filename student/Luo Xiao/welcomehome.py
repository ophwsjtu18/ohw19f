from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
opened_file = open('C:\study\py\sum.csv')
from csv import reader
read_file = reader(opened_file)
su = list(read_file)

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            for a in su[2]:
                ser.write(a.encode())
                time.sleep(3)
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0

    else:
        stayed_time=0
        
     
