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
        self.buildall_3()
        self.list_3 = []
        for i in range(3):
            self.list_3.append(self.data[i])
    def roof(self,x_1,y_1,z_1):
        x0 = x_1
        y0 = y_1
        z0 = z_1   
        long = self.long
        width = self.width
        print("yes")
        for x in range(long):
            for z in range(width):
                mc.setBlock(x0+x,y0,z+z0,block.GLASS.id)
                mc.setBlock(x0+x,y0+self.high-1,z+z0,block.GLASS.id)
                
    
    def buildwall(self,x,y,z):
        x0 = x
        y0 = y
        z0 = z
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

    def buildall_3(self):
        x = self.data[0]
        for i in range(3):
            self.buildall(x+i*self.long+1,self.data[1],self.data[2])
        
    def buildall(self,x0,y0,z0):
        x = x0
        y = y0
        z = z0
        self.roof(x,y,z)
        self.buildwall(x,y,z)

mh = House([pos.x,pos.y,pos.z],15,15,15)
