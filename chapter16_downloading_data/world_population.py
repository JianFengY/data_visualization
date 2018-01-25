# -*- coding: utf-8 -*-
'''
Created on 2018年1月24日

@author: Jeff Yang
'''

import json
import pygal.maps.world
# 从style模块导入样式RotateStyle和加亮颜色的样式
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from chapter16_downloading_data.country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)  # json.load()将数据转换为python能处理的格式，这里是一个列表，存在pop_data中

# 创建一个包含人口数量的字典
cc_populations = {}
# 要用pygal制作地图，要以数字表示人口数量，国别码表示国家，pygal使用两个字母的国别码
# 获取每个国家2010年的人口数量
for pop_dict in pop_data:  # pop_data中每个元素都是一个字典
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # 先用float()再用int()转换为数字，因为python不能直接将包含小数点的字符串转换为整数
        # float()转换为浮点数后int()去除小数部分返回整数
        population = int(float(pop_dict['Value']))
#         print(country_name + ": " + str(population))  # 但是输出需要转换为字符串
        code = get_country_code(country_name)
        if code:
#             print(code + ": " + str(population))
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)

# 根据人口数量将所有国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 传递一个十六进制的RGB颜色（#号开头的字符串，后面每两个字符分别为红绿蓝颜色分量取值00-FF）LightColorizedStyle加亮
wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)  # 传递style实参
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
