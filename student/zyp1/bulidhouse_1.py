import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

class House():
    def __init__(self,data,long,width,high):
        self.data = data
        self.long = long
        self.width = width
        self.high = high
        self.buildall()
        self.list_3 = []
        
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        long = self.long
        width = self.width
        print("yes")
        for x in range(long):
            for z in range(width):
                mc.setBlock(x0+x,y0,z+z0,block.GLASS.id)
                mc.setBlock(x0+x,y0+self.high-1,z+z0,block.GLASS.id)

    def buildwall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x_1 in range(self.long):
            for y_1 in range(self.high):
                mc.setBlock(x0+x_1,y0+y_1,z0,block.GOLD_BLOCK.id)
                print("yeswall")
        for x_1 in range(self.long):
            for y_1 in range(self.high):
                mc.setBlock(x0+x_1,y0+y_1,z0+self.width,block.DIAMOND_BLOCK.id)
                print("yeswall")
        for y_1 in range(self.high):
            for z_1 in range(self.width):
                mc.setBlock(x0,y0+y_1,z0+z_1,block.GLASS.id)
                print("yeswall")
        for y_1 in range(self.high):
            for z_1 in range(self.width):
                mc.setBlock(x0+self.long,y0+y_1,z0+z_1,block.GLASS.id)
                print("yeswall")
        
    def buildall(self):
        
        self.roof()
        self.buildwall()
for i in range(3):
    mh = House([pos.x+i*17,pos.y+i*17,pos.z+i*17],15,15,15)
