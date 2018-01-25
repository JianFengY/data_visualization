# -*- coding: utf-8 -*-
'''
Created on 2018年1月25日

@author: Jeff Yang
'''

# pygal使用的国别码存储在i18n模块中
# 字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
