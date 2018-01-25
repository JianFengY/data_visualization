# -*- coding: utf-8 -*-
'''
Created on 2018年1月25日

@author: Jeff Yang
'''

import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
# 第二个实参传递一个字典，两个字母的国别码作为键，人口数量作为值，pygal根据数字着色，人口少的国家颜色浅
wm.add('North America', {'ca':34126000, 'us':309349000, 'mx':113423000})

wm.render_to_file('na_populations.svg')
