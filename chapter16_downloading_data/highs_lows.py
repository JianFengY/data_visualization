# -*- coding: utf-8 -*-
'''
Created on 2018年1月24日

@author: Jeff Yang
'''

import csv  # python标准库
from matplotlib import pyplot as plt
from datetime import datetime  # 导入datetime模块的datetime类

# 从文件中获取日期、最高气温和最低气温
# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # csv.reader()创建一个与该文件相关联的阅读器对象
    header_row = next(reader)  # next()返回文件的下一行，以逗号分隔的第一行数据

#     # enumerate()获取索引及值
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:  # 遍历文件余下各行，因为第一行是标签
        try:
            # strptime()方法包含所需日期的字符串为第一个实参，第二个实参指定如何设置格式，把字符串转换为datetime格式
            # ‘%Y-’表示第一个连字符前面的作为年份，‘%m-’表示第二个连字符前面的作为月份，‘%d’表示最后部分作为天
            # %A-星期的名称如Monday，%B-月份名如January，%m-数字表示月份（01-12），%d-数字表示天（01-31）
            # %Y-四位的年份如2015，%y-两位的年份如15，%H-24小时制（00-23），%I-12小时制（01-12）
            # %p-am或pm，%M-分钟数（00-59），%S-秒数（00-61）
            current_date = datetime.strptime(row[0], "%Y-%m-%d")  # 日期在第一列
            high = int(row[1])  # 从上面的索引值可以看到最高气温在第2列
            low = int(row[3])  # 从上面的索引值可以看到最低气温在第4列
        except ValueError:
            print(current_date, 'missing data!')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha指定透明度，0为完全透明，默认1为不透明
plt.plot(dates, lows, c='blue', alpha=0.5)
# fill_between()着色，传递x值系列，两个y值系列的部分将被facecolor指定的颜色填充
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期标签，以免重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
