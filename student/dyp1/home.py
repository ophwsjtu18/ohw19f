from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
mc.player.setTilePos([100,150,500])
class HOUSE():
    def __init__(self,data):
        self.data = data

    def roof(self):
        x0 = self.data[0]
        y0 = self.data[1]
        z0 = self.data[2]
        for x in range(11):
            for z in range(11):
                
                    mc.setBlock(x0-10+x,y0+4,z+z0-5,4)
                    mc.setBlock(x0-10+x,y0-1,z+z0-5,4)
                

    def buildWall(self):
         x0=self.data[0]
         y0=self.data[1]
         z0=self.data[2]
         for y in range(4):
             for x in range(11):
                   if x==0 or x==10:
                     for z in range(11):
                         
                             mc.setBlock(x0-10,y0+y,z+z0-5,5)
                             mc.setBlock(x0,y0+y,z+z0-5,5)
                         

                   else:
                      
                          mc.setBlock(x0-10+x,y0+y,z+z0-5,5)
                          mc.setBlock(x0-10+x,y0+y,z+z0-15,5)
                      

         
    
                      
              
mh=HOUSE([100,150,500])
mh.roof()
mh.buildWall()

      
                    
                    
                
            


     
