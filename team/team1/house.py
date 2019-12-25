import mcpi.minecraft as minecraft
import mcpi.block as block

class House():
    def __init__(self, mc, data):
        self.mc = mc
        self.data = data
    
    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        # pat = [[1,1,1,1,1,1,1,1,1,1,1],
        #        [1,2,2,2,2,1,1,0,0,0,1],
        #        [1,2,2,2,2,1,1,0,0,0,1],
        #        [1,2,2,2,2,1,1,0,0,0,1],
        #        [1,2,2,2,2,1,1,0,0,0,1],
        #        [1,1,1,1,1,1,1,0,0,0,1],
        #        [1,1,1,1,1,1,1,0,0,0,1],
        #        [1,1,1,1,1,1,1,0,0,0,1],
        #        [1,1,1,1,1,1,1,0,0,0,1],
        #        [1,1,1,1,1,1,1,0,0,0,1],
        #        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        for x in range(12):
            for z in range(11):
                # if pat[x][z] == 0:
                #     self.mc.setBlock(x-11+x0, y0+10, z-10+z0, block.GLASS.id)
                    # self.mc.setBlock(x - 11 + x0, y0, z - 10 + z0, block.GLASS.id)
                # elif pat[x][z] == 2:
                #     self.mc.setBlock(x-11+x0, y0+10, z-10+z0, block.DIAMOND_BLOCK.id)
                    # self.mc.setBlock(x - 11 + x0, y0, z - 10 + z0, block.DIAMOND_BLOCK.id)
                # else:
                self.mc.setBlock(x-11+x0, y0+10, z-10+z0, block.GOLD_BLOCK.id)
                self.mc.setBlock(x - 11 + x0, y0 , z - 10 + z0, block.GRASS.id)
                    # self.mc.setBlock(x - 11 + x0, y0, z - 11 + z0, block.GOLD_BLOCK.id)


    def wall(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for y in range(10):
            for x in range(11):
                if y>=1 and y<= 8:
                    if x>=1 and x<=5:
                        self.mc.setBlock(x0-11+x, y0+y, z0, block.AIR.id)
                    elif x >=7 and x<=9 and y>=4 and y<=7:
                        self.mc.setBlock(x0-11+x, y0+y, z0, block.GLASS.id)
                    else:
                        self.mc.setBlock(x0 - 11 + x, y0 + y, z0, block.REDSTONE_ORE.id)
                else:
                    self.mc.setBlock(x0 - 11 + x, y0 + y, z0, block.REDSTONE_ORE.id)
                self.mc.setBlock(x0-11+x, y0+y, z0-10, block.REDSTONE_ORE.id)
            for z in range(11):
                self.mc.setBlock(x0, y0+y, z-10+z0, block.REDSTONE_ORE.id)
                self.mc.setBlock(x0-11, y0+y, z-10+z0, block.REDSTONE_ORE.id)
        self.mc.setBlock(x0-10, y0+9, z0+1, block.TORCH.id)
        self.mc.setBlock(x0 - 9, y0 + 9, z0 + 1, block.TORCH.id)
        self.mc.setBlock(x0 - 8, y0 + 9, z0 + 1, block.TORCH.id)
        self.mc.setBlock(x0 - 7, y0 + 9, z0 + 1, block.TORCH.id)
        self.mc.setBlock(x0 - 6, y0 + 9, z0 + 1, block.TORCH.id)
        self.mc.setBlock(x0 - 9, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 8, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 7, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 6, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 5, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 4, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 3, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 2, y0 + 9, z0 - 1, block.TORCH.id)
        self.mc.setBlock(x0 - 1, y0 + 9, z0 - 1, block.TORCH.id)

    def build(self):
        self.wall()
        self.roof()

    def inHouse(self, pos):
        if(pos[0]>self.data[0] and pos[0] < self.data[0]+11
           and pos[0]>self.data[0] and pos[0] < self.data[0]+11
           and pos[0]>self.data[0] and pos[0] < self.data[0]+11):
            return True
        else:
            return False
            

