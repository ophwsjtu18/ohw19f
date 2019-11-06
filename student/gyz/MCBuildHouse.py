import mcpi.minecraft as minecraft
import mcpi.block as block


class House():
    def __init__(self,data):
        self.data = data
    
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                #if pat[x][z] == "0"                    //屋顶的pattern
                    mc.setBlock(x0-10+x,y0+4,z+z0-10,block.GLASS.id)
                #elif pat[x][z] == "2"
                #    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)

                # else:
                #     mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD_BLOCK.id)

    def ground(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(13):
            for z in range(13):
                #if pat[x][z] == "0"                    //屋顶的pattern
                    mc.setBlock(x0-11+x,y0-1,z+z0-11,block.SANDSTONE.id)
                #elif pat[x][z] == "2"
                #    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)

                # else:
                #     mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD_BLOCK.id)

    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(5):
            for x in range(13):
                if x == 0:
                    for z in range(13):
                        mc.setBlock(x0-11+x,y0+y,z0-11+z,block.BRICK_BLOCK.id)
                elif x == 12:
                    for z in range(13):
                        mc.setBlock(x0-11+x,y0+y,z0-11+z,block.BRICK_BLOCK.id)
                else:
                    mc.setBlock(x0-11+x,y0+y,z0-11,block.BRICK_BLOCK.id)
                    mc.setBlock(x0-11+x,y0+y,z0+1,block.BRICK_BLOCK.id)

    def window(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(2):
            for y in range(2):
                mc.setBlock(x0-6+x,y0+1+y,z0-11,block.GLASS_PANE.id)
        
        for x in range(2):
            for y in range(2):
                mc.setBlock(x0-6+x,y0+1+y,z0+1,block.GLASS_PANE.id)
        
        for z in range(2):
            for y in range(2):
                mc.setBlock(x0+1,y0+1+y,z0-6+z,block.GLASS_PANE.id)
        
        for z in range(3):
            for y in range(3):
                mc.setBlock(x0-11,y0+y,z0-6+z,block.AIR.id)

    def buildALL(self):
        self.wall()
        self.roof()
        self.window()
        self.ground()


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

mh = House([pos.x,pos.y,pos.z])
# mh.wall()
# mh.roof()
# mh.window()
# mh.ground()
mh.buildALL()