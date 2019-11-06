import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

class house():
    def __init__(self, data):
        self.data = data

    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(10):
            for z in range(10):
                #if pat[x][z] == "0":
                #mc.setBlock(x0-10+x, 4, z+z0-5, block.GLASS.id)
                #mc.setBlock(x0-10+x, 4, z+z0-5, block.DIAMOND_BLOCK.id)
                mc.setBlock(x0+x, y0+10, z+z0, block.DIAMOND_BLOCK.id)

    def floor(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(10):
            for z in range(10):
                mc.setBlock(x0+x, y0, z0+z, 1)

    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(10):
            for y in range(10):
                mc.setBlock(x0+x, y0+y, z0, 1)
        for x in range(10):
            for y in range(10):
                mc.setBlock(x0+x, y0+y, z0+9, 1)
        for z in range(10):
            for y in range(10):
                mc.setBlock(x0, y0+y, z0+z, 1)
        for z in range(10):
            for y in range(10):
                mc.setBlock(x0+9, y0+y, z0+z, 1)

    def windous(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(2):
            for z in range(2):
                mc.setBlock(x0, y0+3+y, z0+5+z, block.GLASS.id)

    def door(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(2):
            for y in range(3):
                mc.setBlock(x0+5+x, y0+y, z0, block.GLASS.id)

if __name__ == "__main__":
    pos = mc.player.getTilePos()
    mh = house([pos.x, pos.y, pos.z])
    print(pos)
    mh.roof()
    mh.floor()
    mh.wall()
    mh.windous()
    mh.door()
    mh1 = house([pos.x+20, pos.y, pos.z+20])
    mh1.roof()
    mh1.floor()
    mh1.wall()
    mh1.windous()
    mh1.door()
    mh2 = house([pos.x+40, pos.y, pos.z+40])
    mh2.roof()
    mh2.floor()
    mh2.wall()
    mh2.windous()
    mh2.door()


