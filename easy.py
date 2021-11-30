#这里是简单图形文件，以模块型使用
'''
图形列表
1.漩涡
'''
from turtle import *
# 漩涡

def wirlpool(n): #转动次数
  for i in range(n):
    forward(i)
    left(59)
