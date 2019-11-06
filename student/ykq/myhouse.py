class House():
    def __init__(self,data,h):
        self.data=data
        self.h=h
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for i in range(10):
            for j in range(self.h):
                mc.setBlock(x0+i,y0+j,z0+j, block.STONE.id)
    def buildWall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for i in range(10):
            for j in range(self.h):
                mc.setBlock(x0+i, y0+j, z0, block.STONE.id)
                mc.setBlock(x0+i, y0+j, z0+10, block.STONE.id)
                mc.setBlock(x0, y0+j, z0+i, block.STONE.id)
                mc.setBlock(x0+10, y0+j, z0+i, block.STONE.id)
        for z in range(2):
                for y in range(2): 
                    mc.setBlock(x0+10, y0+y+2, z0+z+4, block.GLASS.id)


    def buildAll(self):
        self.buildWall()
        self.roof()
        
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

h1=House([pos.x,pos.y,pos.z],6)
h1.buildAll()
h2=House([pos.x+20,pos.y,pos.z],8)
h2.buildAll()
h3=House([pos.x+30,pos.y,pos.z],10)
h3.buildAll()
