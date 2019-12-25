# Author: Kang Huquan & Girafboy
# encoding:utf-8

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

from model import Model
from house import House

mc=minecraft.Minecraft.create("127.0.0.3", 4711)


pos = mc.player.getTilePos()
house1 = House(mc,[pos.x, pos.y, pos.z])
house2 = House(mc,[pos.x+50, pos.y, pos.z])
house3 = House(mc,[pos.x+100, pos.y, pos.z])
house1.build()
house2.build()
house3.build()
model1 = Model(mc,'chiji.binvox')
model2 = Model(mc,'guidaopao.binvox')
model3 = Model(mc,'mickey__mouse_hoofd.binvox')
model1.build([pos.x-15, pos.y, pos.z+10])
model2.build([pos.x+35, pos.y, pos.z+10])
model3.build([pos.x+85, pos.y, pos.z+10])


