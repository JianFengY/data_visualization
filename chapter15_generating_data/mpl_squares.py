# -*- coding: utf-8 -*-
'''
Created on 2018年1月23日

@author: Jeff Yang
'''

import matplotlib.pyplot as plt  # 模块pyplot包含很多用于生成图表的函数

input_values = [1, 2, 3, 4, 5]  # 不设置输入值的话，x轴的默认初始值是0，图表会有错误
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # 尝试根据这些数绘制折线图，linewidth指定线条粗细

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)  # 标题，fontsize指定文字大小
plt.xlabel("Value", fontsize=14)  # x轴标题
plt.ylabel("Aquare of Value", fontsize=14)  # y轴标题

# 设置刻度标记大小
# tick_params()设置刻度样式，axis='both'表示x和y轴都改变，对应的，还有axis='x'，axis='y'
plt.tick_params(axis='both', labelsize=14)

plt.show()  # 打开matplotlib查看器
