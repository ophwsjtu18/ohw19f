class house():
    def __init__(self,data):
        self.data=data
        
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        pat = [[1,1,1,1,1,1,1,1,1,1,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,2,2,2,2,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1]]
        for x in range(11):
            for z in range(11):
                if pat[x][z] == 0:
                    mc.setBlock(x-11+x0, y0+20, z-11+z0, block.GLASS.id)
                elif pat[x][z] == 2:
                    mc.setBlock(x-11+x0, y0+20, z-11+z0, block.DIAMOND_BLOCK.id)
                else:
                    mc.setBlock(x-11+x0, y0+20, z-11+z0, block.GOLD_BLOCK.id)
    def buildWall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(20):
            for x in range(11):
                mc.setBlock(x0-11+x, y0+y, z0, block.GLASS.id)
                mc.setBlock(x0-11+x, y0+y, z0-11, block.GLASS.id)
            for z in range(11):
                mc.setBlock(x0, y0+y, z-11+z0, block.GLASS.id)
                mc.setBlock(x0-11, y0+y, z-11+z0, block.GLASS.id)
    def buildAll(self):
        self.roof()
        self.buildWall()
        
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mh1=house([pos.x,pos.y,pos.z])
mh1.buildAll()
mh2=house([pos.x+30,pos.y,pos.z+30])
mh2.buildAll()
mh3=house([pos.x-30,pos.y,pos.z-30])
mh3.buildAll()
