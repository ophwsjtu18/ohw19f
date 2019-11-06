# Author: Kang Huquan & Girafboy

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc=minecraft.Minecraft.create("127.0.0.3", 4711)


class House():
    def __init__(self, data):
        self.data = data
    
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


    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(20):
            for x in range(11):
                mc.setBlock(x0-11+x, y0+y, z0, block.GRASS.id)
                mc.setBlock(x0-11+x, y0+y, z0-11, block.GRASS.id)
            for z in range(11):
                mc.setBlock(x0, y0+y, z-11+z0, block.GRASS.id)
                mc.setBlock(x0-11, y0+y, z-11+z0, block.GRASS.id)

    def build(self):
        self.wall()
        self.roof()


pos = mc.player.getTilePos()
house1 = House([pos.x, pos.y, pos.z])
house2 = House([pos.x+20, pos.y, pos.z])
house3 = House([pos.x+40, pos.y, pos.z])
house1.build()
house2.build()
house3.build()
