import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
position=list(pos)
position1=list(range(3))
position2=list(range(3))

for i in range(3):
    position1[i]=list(pos)[i]+25
    position2[i]=list(pos)[i]-25

position1[1]=list(pos)[1]
position2[1]=list(pos)[1]

class House():
    def __init__(self,data):
        self.data=data
    def roof(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for x in range(11):
            for z in range(11):
                mc.setBlock(x0+x,y0+8,z+z0-5,57)
                    
    def wall(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(9):
            for z in range(11):
                mc.setBlock(x0,y+y0,z+z0-5,41)
                mc.setBlock(x0+10,y+y0,z+z0-5,41)
        for y in range(9):
            for x in range(10):
                mc.setBlock(x0+x+1,y+y0,z0-5,41)
                mc.setBlock(x0+x+1,y+y0,z0+5,41)
                    
    def door(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]
        for y in range(5):
            mc.setBlock(x0+4,y+y0,z0-5,20)
            mc.setBlock(x0+5,y+y0,z0-5,20)

                    

mh=House(position)
mh.wall()
mh.roof()
mh.door()
mh1=House(position1)
mh1.wall()
mh1.roof()
mh1.door()
mh2=House(position2)
mh2.wall()
mh2.roof()
mh2.door()