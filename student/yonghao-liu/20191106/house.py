import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

class House():
    def __init__(self, data):
        self.data = data
    def roof(self): # Build a roof
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for j in range(11):
                mc.setBlock(x0+x,y0+y,z,57)
                
position = House(pos)
position.roof()