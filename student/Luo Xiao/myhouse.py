import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

import mcpi.block as block

class house():
    def __init__(self,data):
        self.data=data

    def roof(self):
        for x in range(11):
            for z in range(11):
                mc.setBlock(pos.x+x,pos.y+10,pos.z+z,block.WOOD.id)
    def floor(self):
        for x in range(11):
            for z in range(11):
                mc.setBlock(pos.x+x,pos.y,pos.z+z,block.WOOD.id)
    def wall(self):
        for x in range(11):
            for y in range(11):
                for z in range(11):
                    mc.setBlock(pos.x+x,pos.y+y,pos.z,block.GLASS.id)
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+10,block.GLASS.id)
                    mc.setBlock(pos.x,pos.y+y,pos.z+z,block.GLASS.id)
                    mc.setBlock(pos.x+10,pos.y+y,pos.z+z,block.GLASS.id)
    def door(self):
        mc.setBlock(pos.x+5,pos.y,pos.z,block.DOOR.id)

                    block.
mh=house(pos)
mh.roof()
mh.floor()
mh.wall()


