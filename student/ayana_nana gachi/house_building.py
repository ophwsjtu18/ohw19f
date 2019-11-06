import mcpi.minecraft as minecraft
import mcpi.block as block

import time
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()

Material=[block.IRON_BLOCK.id,block.WOOD.id,block.SNOW_BLOCK.id]

pat=[
[1,1,1,1,1,1,1,1,1,1],
[1,3,3,3,3,3,3,3,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,1,1,3,3,3,1,3,1],
[1,3,1,1,3,1,3,1,3,1],
[1,3,1,1,3,3,3,1,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,1,1,1,1,1,1,3,1],
[1,3,3,3,3,3,3,3,3,1],
[1,1,1,1,1,1,1,1,1,1]]

def house(x0,y0,z0,M=block.SNOW_BLOCK.id,L=10,W=10,H=10,):
    for a in range(0,L):
        for c in range(0,W):
            for b in range(0,H):
                mc.setBlock(x0+a,y0+b,z0+c,M)                 #先填满
    for a in range(0,L-2):
        for c in range(0,W-2):
            for b in range(0,H-1):
                mc.setBlock(x0+1+a,y0+1+b,z0+1+c,0)           #再清除内部
    for a in range(0,L):
        for b in range(0,W):
            if pat[a][b]==1:
                mc.setBlock(x0+a,y0+H,z0+b,block.GLASS.id)        #天花板透明
            else:
                mc.setBlock(x0+a,y0+H,z0+b,block.DIAMOND_BLOCK.id)
    for a in range(1,3):
        x1=int((2*x0+L)/2)
        mc.setBlock(x1,y0+a,z0,0)                             #造个门
    x1=int(x0+L/4)
    y1=int(y0+H/2)
    mc.setBlock(x1,y1,z0,block.GLASS.id)                                   #开个窗户

house(pos.x,pos.y,pos.z,Material[0])
house(pos.x+15,pos.y,pos.z,Material[1])                         #造三个房子，状态不一样
house(pos.x-15,pos.y,pos.z,Material[2])

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))