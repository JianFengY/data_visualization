# -*- coding: utf-8 -*-
'''
Created on 2018年1月25日

@author: Jeff Yang
'''

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
# https://api.github.com 可以看到各个API的调用方法
# https://api.github.com/rate_limit 可以看到API的速率限制
# github API，search/repositories让API搜索github上所有的仓库
# q=language:python，q表示查询，language指定语言，sort=stars指定根据stars数排序
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)  # 状态码200表示成功

# 将API响应存储在一个变量中
response_dict = r.json()  # json()将信息转换为一个字典
# # 处理结果
# print(response_dict.keys())  # 打印出键
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

# 列表plot_dicts存放star数和工具提示
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],  # star数
        # 项目描述，防止有项目没有description的报错
        'label':repo_dict['description'] if repo_dict['description'] 
            else 'There is no description about this project',
        'xlink':repo_dict['html_url']  # 将条形转换为相应的链接，链接到相应的github页面
        }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)  # 基色设置为深蓝

my_config = pygal.Config()
my_config.x_label_rotation = 45  # 让标签绕x轴旋转45度
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 标题字体大小
my_config.label_font_size = 14  # 副标签字体大小（这里是x轴上的项目名及y轴上的大部分数字）
my_config.major_label_font_size = 18  # 主标签字体大小（y轴上5000整数倍的刻度，比副标签更大方便区分）
my_config.truncate_label = 15  # 将较长项目名称缩短为15个字符，用鼠标指向截短的项目名显示完整
my_config.show_y_guides = False  # 隐藏水平线
my_config.width = 1000  # 自定义宽度

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
