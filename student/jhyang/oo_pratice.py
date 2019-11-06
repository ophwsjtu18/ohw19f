import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

class House():
    def __init__(self, data):
        self.data = data 
        self.pos = data

    def getPos(self):
        pos = mc.player.getTilePos()
        self.pos[0]=self.pos[0]+pos[0]
        self.pos[1]=self.pos[1]+pos[1]
        self.pos[2]=self.pos[2]+pos[2]
        #print(self.pos) 
    def buildRoof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(9):
            for y in range(9):
                mc.setBlock(x0+x,y0+y,z0,25)
    
    def buildColumn(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for z in range(z0-1):
            mc.setBlock(x0+4,y0+4,z,25)
            mc.setBlock(x0+5,y0+5,z,25)
'''
    def buildAll(self):
        buildRoof(self)
        buildAll(self)

mh1 = House([100,200,50])
mh1.buildRoof()

mh2 = House([120,180,50])
mh2.buildColumn()
'''
mh3 = House([150,150,50])
mh3.getPos()
