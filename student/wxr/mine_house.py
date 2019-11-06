import mcpi.minecraft as minecraft
import mcpi.block as block 
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos() 

class House():
    def __init__(self,data,pat):
        self.data=data
        self.pat=pat
    def roof(self,pat):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(6):
            for z in range(6):
                if(pat[z]==0):
                    mc.setBlock(x0-5+x,y0+5,z0-5+z,block.DIAMOND_BLOCK.id)
                else:
                    mc.setBlock(x0 - 5 + x, y0 + 5, z0 - 5 + z, block.STONE_BRICK.id)

                mc.setBlock(x0 - 5 + x, y0 + 6, z0 - 5 + z, block.TORCH.id)


    def wall(self,pat):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]

        for x in range(5):
            for y in range(5):
                mc.setBlock(x0 - 5 + x, y0 + 4 - y, z0, block.GOLD_BLOCK.id)
                mc.setBlock(x0 - 5 + x, y0 + 4 - y, z0 - 5, block.GOLD_BLOCK.id)

        mc.setBlock(x0-5, y0, z0 - 3, block.IRON_BLOCK.id)
        mc.setBlock(x0 - 5, y0+1, z0 - 3, block.IRON_BLOCK.id)
        mc.setBlock(x0 - 5, y0, z0 - 2, block.IRON_BLOCK.id)
        mc.setBlock(x0 - 5, y0 + 1, z0 - 2, block.IRON_BLOCK.id)

    def build_all(self,pat):
        self.wall(self.pat)
        self.roof(self.pat)

pat1=[1,0,1,0,1,0]
pat2=[1,1,1,0,0,0]
pat3=[1,0,0,0,0,1]

h1=House([pos.x+10,pos.y,pos.z],pat1)
h2=House([pos.x+18,pos.y,pos.z],pat2)
h3=House([pos.x+10,pos.y,pos.z+10],pat3)
h1.build_all(pat1)
h2.build_all(pat2)
h3.build_all(pat3)

