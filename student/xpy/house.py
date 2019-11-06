from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports
from csv import reader
class house():
    def __init__(self,data):
        self.data=data
    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        i=0
        while(i<4):
            i+=1
            for x in range(11):
                if x<4 or x>6:
                    mc.setBlock(x0-10+x,y0-i,z0,3)
                else:
                    mc.setBlock(x0-10+x,y0-i,z0,324)

    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0-10+x,y0,z0-10+z,1)
                
    def buildwall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        i=0
        while(i<4):
            i+=1
            for x in range(11):
                mc.setBlock(x0-10+x,y0-i,z0-10,3)
            for z in range(11):
                mc.setBlock(x0-10,y0-i,z0-10+z,3)
                if (z<4 or z>6) and (i==1 or i==4):
                    mc.setBlock(x0,y0-i,z0-10+z,3)
                else:
                    mc.setBlock(x0,y0-i,z0-10+z,20)

            for x in range(11):
                for z in range(11):
                    mc.setBlock(x0-10+x,y0-5,z0-10+z,1)
    def buildall(self):
        self.roof()
        self.buildwall()
        self.door()
    def buildthree(self):
        self.buildall()
        self.data[0]-=10
        self.buildall()
        self.data[0]-=10
        self.buildall()
        
        
mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0
mh=house([-181,15,399])
mh.buildthree()
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
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0

    else:
        stayed_time=0
        
     
