# -*- coding: utf-8 -*-
'''
Created on 2018年1月25日

@author: Jeff Yang
'''

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# pygal中，将鼠标指向条形将显示它的信息，这称为工具提示

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_label = ['awesome-python', 'httpie', 'youtube-dl']

plot_dicts = [
    # 根据value的值创建高度，根据label的值创建工具提示
    {'value':44399, 'label':'Description of awesome-python'},
    {'value':33564, 'label':'Description of httpie'},
    {'value':33293, 'label':'Description of youtube-dl'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
