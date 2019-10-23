# ohw19f
Open source maker course for SJTU in 2019 fall

# 串口钢琴Mixly代码

 参考

![](https://github.com/ophwsjtu18/ohw19/blob/master/serp_mixly.PNG)

# 安装串口包

pip install pyserial




# 设置pip安装源为国内

安装步骤：  

在你的电脑的c:\user(或者用户)\你电脑的用户名\，这个目录下创建个命名为“pip”的文件夹（如：C:\Users\gmn\pip），在该文件夹下创建一个命名为“pip.ini”的文件，在该文件中写入以下内容：  

[global]  
index-url=https://mirrors.aliyun.com/pypi/simple/  
[install]    
trusted-host=https://mirrors.aliyun.com/pypi/simple/    
disable-pip-version-check = true    
timeout = 6000  

# OpenCV 

打开cmd  或 powershell  
pip install opencv-python

# Git 设置

git config --global user.name “Your Name”  
git config --global user.email youremail@whatever.com  
git config -- list  
git config -- global credential.helper 'cache --timeout 3600'  

# OpenCV 读图形

 import  cv2  
img=cv2.imread("aa.jpg" )  
 cv2.imshow("wwww",img)  
 cv2.waitKey(0)  
 cv2.destroyAllWindows()  
 
