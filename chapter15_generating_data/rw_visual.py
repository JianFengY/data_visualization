# -*- coding: utf-8 -*-
'''
Created on 2018年1月24日

@author: Jeff Yang
'''

import matplotlib.pyplot as plt

from chapter15_generating_data.random_walk import RandomWalk

# 只要程序处于活动状态，就不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例，指定num_points为50000，并将其中的点绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # 设置绘图窗口的尺寸
    # figure()指定宽度、高度、分辨率和背景色，需要给形参figsize指定一个元组
    # 如果知道系统屏幕分辨率，可以使用形参dpi传递改分辨率，如plt.figure(dpi=128, figsize=(10, 6))
    plt.figure(figsize=(10, 6))
    
    points_numbers = list(range(rw.num_points))
    # c为步数，这样步数值大的颜色深，也就是漫步轨迹由浅到深
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Reds,
        edgecolors='none', s=1)
    plt.colorbar()  # 添加一个颜色条
    
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black',
        edgecolors='none', s=50)
    
    # 隐藏坐标轴（控制台会出现一个警告，但可忽略）
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
