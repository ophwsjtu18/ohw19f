import mcpi.minecraft as minecraft
import mcpi.block as block

class House():
    def __init__(self,data,pat):
        self.data=data
        self.pat=pat
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                if self.pat[x][z]=="0":
                    mc.setBlock(x0-10+x,y0+4,z+z0-5,block.GLASS.id)
                elif self.pat[x][z]=="2":
                    mc.setBlock(x0-10+x,y0+4,z0-5,block.DIAMOND_BLOCK.id)
                else:
                    mc.setBlock(x0-10+x,y0+4,z+z0-5,block.GOLD_BLOCK.id)
    def buildWall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(2):
            for y in range(4):
                for z in range(11):
                    mc.setBlock(x0-10+x*10,y0+y,z+z0-5,block.DIAMOND_BLOCK.id)
        for z in range(2):
            for y in range (4):
                for x in range(11):
                    mc.setBlock(x0-10+x,y0+y,z*10+z0-5,block.GLASS.id)
    def buildAll(self):
        self.roof()
        self.buildWall()
pat=11*[11*["1"]]
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
pos_1=list(pos)
#myhouse=House(list(pos),pat)
#myhouse.roof()
#myhouse.buildWall()
#myhouse.buildAll()

for i in range(3):
    x=pos_1[0]+12*i
    y=pos_1[1]
    z=pos_1[2]+12*i
    pos_2=[x,y,z]
    myhouse=House(pos_2,pat)
    myhouse.buildAll()

