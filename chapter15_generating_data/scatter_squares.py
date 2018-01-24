# -*- coding: utf-8 -*-
'''
Created on 2018年1月24日

@author: Jeff Yang
'''

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]  # 列表解析

# scatter()绘制散点图
# s为点的尺寸，edgecolor为点的轮廓颜色
# c为点的颜色，可以用RGB定义颜色，传递一个包含三个0到1间小数值的元组，分别表示红绿蓝颜色分量，越接近0颜色越深，也可以直接c='red'
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# cmap颜色映射（colormap)，颜色从起始渐变到结束，根据y值用蓝色渐变
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Aquare of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])  # x和y轴的最小值和最大值，x轴取值为0到1100y轴为0到1100000

# 设置刻度标记大小
# which默认是major表示主刻度，minor为次刻度，both为主次刻度都显示
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
# 保存图片，bbox_inches='tight'指定裁剪周围空白区域
# plt.savefig('squares_plot.png', bbox_inches='tight')
