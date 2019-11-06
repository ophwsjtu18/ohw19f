from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()
#mc=Minecraft.create("10.163.80.195",4711)\

class HOUSE():
    def __init__(self,data):
        self.data = data
    def ground(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                    mc.setBlock(x0+x,y0,z0+z,1)
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                    mc.setBlock(x0+x,y0+5,z0+z,1)
    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for y in range(5):
                    mc.setBlock(x0+x,y0+y,z0,1)
                    mc.setBlock(x0+x,y0+y,z0+10,1)
                    mc.setBlock(x0,y0+y,z0+x,1)
                    mc.setBlock(x0+10,y0+y,z0+x,1)
    def decoration(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range (2):
            for y in range(2):
                mc.setBlock(x0+3+x,y0+3+y,z0,20)
                mc.setBlock(x0+7+x,y0+3+y,z0,20)
        mc.setBlock(x0+1,y0+1,z0,76)
        mc.setBlock(x0+1,y0+2,z0,76)#doorwithtorch
        mc.setBlock(x0+5,y0+5,z0+5,89)#stone to light
        for x in range(11):
            mc.setBlock(x0+x,y0+6,z0,50)
            mc.setBlock(x0+x,y0+6,z0+10,50)
            mc.setBlock(x0,y0+6,z0+x,50)
            mc.setBlock(x0+10,y0+6,z0+x,50)

        
    def work(self):
        self.roof()
        self.wall()
        self.ground()
        self.decoration()

mh1 = HOUSE([pos.x,pos.y-1,pos.z])
mh1.work()
mh2 = HOUSE([pos.x+15,pos.y-1,pos.z])
mh2.work()
mh3 = HOUSE([pos.x+30,pos.y-1,pos.z])
mh3.work()
