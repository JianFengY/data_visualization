# -*- coding: utf-8 -*-
'''
Created on 2018年1月24日

@author: Jeff Yang
'''

# 可视化包pygal生成可缩放的矢量图形文件，对于需要在尺寸不同的屏幕上显示的图表很有用
import pygal
from chapter15_generating_data.Die import Die

# 创建一个D6骰子和一个D10骰子
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []  # 存储每种结果出现的点数

max_result = die_1.num_sides + die_2.num_sides  # 两个骰子所能得到的最大点数
for value in range(2, max_result + 1):
    frequency = results.count(value)  # 计算各个点数出现的次数
    frequencies.append(frequency)
    
# 对结果进行可视化
hist = pygal.Bar()  # 创建条形图

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency"

# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个包含将出现在图标中的值）
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')  # 渲染为.svg文件
