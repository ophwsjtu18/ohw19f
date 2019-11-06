import mcpi.block as block
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


x0=pos.x
y0=pos.y
z0=pos.z

class House():
    def _init_(self,data):
        self.data=data
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                if pat[x][z]=="0":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GLASS.id)
                elif pat[x][z]=="2":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)
                    
                else:
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD_BLOCK.id)

            
for b in range(9):
    for a in range(10):
        mc.setBlock(pos.x+a, pos.y+b, pos.z, block.STONE.id)
        mc.setBlock(pos.x+a, pos.y+b, pos.z+9, block.STONE.id)
    for a in range(8):
        mc.setBlock(pos.x, pos.y+b, pos.z+1+a, block.STONE.id)
        mc.setBlock(pos.x+9, pos.y+b, pos.z+1+a, block.STONE.id)

for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x+x, pos.y, pos.z+z, block.STONE.id)

for x in range(10):
    for z  in range(10):
        mc.setBlock(pos.x+x, pos.y+9, pos.z+z, block.STONE.id)
        
for z in range(2):
      for y in range(2): 
            mc.setBlock(pos.x+9, pos.y+y+2, pos.z+z+3, 20)

mc.setBlock(pos.x+5, pos.y+1, pos.z,0)
mc.setBlock(pos.x+5, pos.y+2, pos.z,0)

