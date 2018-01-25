# -*- coding: utf-8 -*-
'''
Created on 2018年1月25日

@author: Jeff Yang
'''

# 绘制地图的模块，有改动，书上的pygal.Worldmap()已经无法使用
from pygal.maps import world

wm = world.World()
wm.title = 'North, Central, and South America'

# add()方法接收一个标签和一个列表，后者包含要突出的国家的国别码
# 每次调用add()都将为指定的国家选择一种新颜色，并在图标左边显示该颜色和指定的标签
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
