蓝灯好像用不了，哭了。能不能解决一下
 软件我安了
 
# jiangfangzi
class house():
    def _init_(self,data):
        self.data = data
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                if pat[x][z] == "0":
                    mc.setBlock(x0-10+x,4,z+z0-5,block,GLASS.id)
                elif pat[x][z] == "z":
                    mc.setBlock(x0-10+x,4,z+z0-5,block.DIAMOND_BLOCK.id)

                else:
                    mc.setBlock(x0-10+x,4,z+z0-5,block.GOLD.BLOCK.id)
