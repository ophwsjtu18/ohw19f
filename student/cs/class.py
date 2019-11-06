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
        for x in range(11):
            for z in range(11):
                if x//2=="0":
                    mc.setBlock(x0-10+x,y0-10+x,z+z0-5,block.GLASS.id)
                else:
                    mc.setBlock(x0-10+x,y0-10+x,z+z0-5,block.GOLD_BLOCK.id)
    def buildAll(self):
        self.roof()
        self.buildWall()
        
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mh=house([pos.x,pos.y,pos.z])
mh.buildAll()
