import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()     
class house():
    def __init__(self,data):
        self.data=data

    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                for y in range(11):
                    mc.setBlock(x+x0,y+y0,z+z0,block.STONE.id)
        for x in range(9):
            for z in range(9):
                for y in range(9):
                    mc.setBlock(x0+1+x,y0+1+y,z0+1+z,block.AIR.id)
        
    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(3):
             mc.setBlock(x0+5,y0+y+1,z0,block.AIR.id)
    def window(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(2):
            for z in range(2):
               mc.setBlock(x0,y0+y+1,z0+3+z,block.GLASS.id) 
    def fire(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
               mc.setBlock(x0+x,y0+11,z0+z,block.GLOWSTONE_BLOCK.id) 
    def build(self):
        self.wall()
        self.window()
        self.door()
        self.fire()

mh=house ([-22,5,3])
mh1=house([20,5,3])
mh2=house([-22,5,30])
mh.build()
mh1.build()
mh2.build()
