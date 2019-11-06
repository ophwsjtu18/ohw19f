import mcpi.minecraft as minecraft
import mcpi.block as block



mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
class house():
    def __init__(self, data):
        self.data = data

    def roof(self, mc, pat):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(10):
            for z in range(10):
                if pat =="0":
                    mc.setBlock(x0-10+x, y0+10, z+z0-5, block.GLASS.id)
                elif pat == "1":
                    mc.setBlock(x0-10+x, y0+10, z+z0-5, block.DIAMOND_BLOCK.id)
                else:
                    mc.setBlock(x0-10+x, y0+10, z+z0-5, block.GOLD_BLOCK.id)
    def ground(self, mc):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(10):
            for z in range(10):
                mc.setBlock(x0-10 + x, y0, z + z0-5, block.GOLD_BLOCK.id)
    def wall(self, mc):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(10):
            for a in range(10):
                mc.setBlock(x0-10 + a, y0 + y, z0-5, block.STONE.id)
                mc.setBlock(x0-10 + a, y0 + y, z0 + 4, block.STONE.id)
            for a in range(8):
                mc.setBlock(x0-10, y0 + y, z0 - 4 + a, block.STONE.id)
                mc.setBlock(x0-1, y0 + y, z0 -4  + a, block.STONE.id)

    def door(self, mc):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(2):
            mc.setBlock(x0 - 5, y0 + 1 + y, z0-5, block.DIAMOND_BLOCK.id)

    def windows(self, mc):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(2):
            for z in range(2):
                mc.setBlock(x0 - 9, 0 + 3 + y0, z - 5 + z0, block.DIAMOND_BLOCK.id)


print(pos)

House = house([pos.x, pos.y, pos.z])
House.roof(mc, '2')
House.ground(mc)
House.wall(mc)
House.door(mc)
House.windows(mc)


House1 = house([pos.x+20, pos.y, pos.z+20])
House1.roof(mc, '2')
House1.ground(mc)
House1.wall(mc)
House1.door(mc)
House1.windows(mc)

House2 = house([pos.x+40, pos.y, pos.z+40])
House2.roof(mc, '2')
House2.ground(mc)
House2.wall(mc)
House2.door(mc)
House2.windows(mc)