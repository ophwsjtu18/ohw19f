 ![Image text](https://github.com/ophwsjtu18/ohw19f/blob/master/student/guiyiliu/TIM截图20191022233123.png)
 ![Image text](https://github.com/ophwsjtu18/ohw19f/blob/master/student/guiyiliu/TIM截图20191022233644.png)
 蓝灯好像用不了，哭了。能不能解决一下
 软件我安了
# -*- coding: utf-8 -*
"""
Created on Sun Jan 5 11:41:39 2014
@author: duan
"""
import cv2
import numpy as np
#当鼠标按下时变为True
drawing=False
如果 mode 为true绘制矩形。按下 'm'变成绘制曲线。
mode=True
ix,iy=-1,-1
#创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
当鼠标左键按下并移动是绘制图形。event 可以查看移动， flag查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线， 3 代表了笔画的粗细
                cv2.circle(img,(x,y),3,(0,0,255),-1)
                # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
                # 当鼠标松开停止绘画。
        elif event==cv2.EVENT_LBUTTONUP:
            drawing==False
            # if mode==True:
                # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            # else:
                # cv2.circle(img,(x,y),5,(0,0,255),-1)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('m'):
        mode=not mode
    elif k==27:
        break

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
