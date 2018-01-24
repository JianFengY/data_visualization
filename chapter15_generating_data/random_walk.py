# -*- coding: utf-8 -*-
'''
Created on 2018年1月24日

@author: Jeff Yang
'''

# 将所有可能的选择存储在列表里，并在每次决策时都使用choice()决定使用哪种选择
from random import choice


class RandomWalk():
    """一个生成随机漫步数据的类"""
    
    def __init__(self, num_points=5000):  # 随机漫步包含的默认点数设置为5000
        """初始化随机漫步的属性"""
        self.num_points = num_points  # 随机漫步次数的变量
        
        # 所有随机漫步都始于(0,0)
        self.x_values = [0]  # 随机漫步经过的每个点的x坐标
        self.y_values = [0]  # 随机漫步经过的每个点的y坐标

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])  # 1表示向右，-1表示像左
            x_distance = choice([0, 1, 2, 4])  # 随机选择向指定方向走多远，0可以设置只沿y轴移动
            x_step = x_direction * x_distance  # 与x_direction相乘用以定向
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 4])
            y_step = y_direction * y_distance
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:  # x和y都为0意味着没有移动
                continue
            
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step  # 与x_values中最后一个值相加决定下一个位置
            next_y = self.y_values[-1] + y_step  # 同理与y_values中最后一个值相加
            
            # 把下一步的位置存储到列表中
            self.x_values.append(next_x)
            self.y_values.append(next_y)
