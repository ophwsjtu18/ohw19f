import mcpi.minecraft as minecraft
import mcpi.block as block

import time
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

Material=[block.GOLD_BLOCK.id,block.STONE.id,block.SNOW_BLOCK.id]


def house(x0,y0,z0,M=block.SNOW_BLOCK.id,L=10,W=10,H=10,):
    for x in range(0,L):
        for y in range(0,W):
            mc.setBlock(x0+x,y0+y,z0,M)  #floor
    for x in range(0,L):
        for y in range(0,W):
            mc.setBlock(x0+x,y0+y,z0+H,M) #roof
    for x in range(0,L):
        for z in range(0,H):
            mc.setBlock(x0+x,y0,z0+z,M)
    for x in range(0,L):
        for z in range(0,H):
            mc.setBlock(x0+x,y0+W,z0+z,M)       #walls
    for z in range(0,H):
        for y in range(0,W):
            mc.setBlock(x0,y0+y,z0+y,M)
    for z in range(0,H):
        for y in range(0,W):
            mc.setBlock(x0+L,y0+y,z0+y,M)

    for a in range(1,3):
        x1=int((2*x0+L)/2)
        mc.setBlock(x1,y0+a,z0,0)
    x1=int(x0+L/4)
    y1=int(y0+H/2)
    mc.setBlock(x1,y1,z0,block.GLASS.id)                            

house(pos.x,pos.y,pos.z,Material[0])
house(pos.x+30,pos.y,pos.z,Material[1]) 
house(pos.x-30,pos.y,pos.z,Material[2])