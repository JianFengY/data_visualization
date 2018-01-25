# -*- coding: utf-8 -*-
'''
Created on 2018年1月25日

@author: Jeff Yang
'''

# pygal使用的国别码存储在i18n模块中，书上的pygal.i18n已经无法使用
# 字典COUNTRIES包含的键和值分别为两个字母的国别码和国家名
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():  # 遍历字典
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))
