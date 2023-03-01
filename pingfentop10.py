# import pymongo
# import collections
from highcharts import  Highchart
#
# db =pymongo.MongoClient('localhost',27017)
# douban = db['douban']
# item_info = douban['top250']
#
#
# #清洗TOP250评分数据排行；
# year_list =[]
# country_list = []
# dict_list = {}
# #提取mongodb数据；
# for i in item_info.find():
#     dict_list[i['name']] = float(i['star'])
#     year_list.append(i['year'])
#     country_list.append(i['country'])
#
# year_dict={}
# for i in year_list:
#     year_dict[i] =year_dict.get(i,0)+1
# print(year_dict)
# tuple_year = sorted(year_dict.items(),key=lambda item:item[0])
# print(tuple_year)
# year_list1 = []
# for j in range(len(tuple_year)):
#     a = int(str(tuple_year[j][0]).strip('\n').strip('\xa0'))
#     b =tuple_year[j][1]
#     list1 = []
#     list1.append(a)
#     list1.append(b)
#     year_list1.append(list1)
# print(year_list1)

#豆瓣电影top10评分代码；
# print(set(year_list),set(country_list))
# sorted_dict=[]
# tuple_list = sorted(dict_list.items(),key = lambda item:item[1],reverse=True)
# for i in range(len(tuple_list)):
#     a = tuple_list[i][0]
#     b = tuple_list[i][1]
#     list=[]
#     list.append(a)
#     list.append(b)
#     sorted_dict.append(list)
# a_list = sorted_dict[:10]






#豆瓣电影top10评分柱状图代码

# H = Highchart(width=850,high = 400)
# options = {
#     'chart': {
#             'type': 'column'
#             # 'style':{'border color':'#a64d79'}
#         },
#         'title': {
#             'text': '豆瓣电影评分top10'
#         },
#         'subtitle': {
#             'text': '数据来源：www.douban.com'},
#
#
#         'xAxis': {
#             'type': 'category',
#             'labels': {
#                 'rotation': -45,
#                 'style': {
#                     'fontSize': '12px',
#                     'fontFamily': 'Verdana, sans-serif'
#                 }
#             }
#         },
#         'yAxis': {
#             'min': 0,
#             'title': {
#                 'text': '电影评分'
#             }
#         },
#         'legend': {
#             'enabled': False
#         },
#         'tooltip': {
#             'pointFormat': 'Population in 2017: <b>{point.y:.1f} millions</b>'
#         },
#
#
# }
#
# H.set_dict_options(options)
# H.add_data_set(a_list,'column',  dataLabels={
#                                'enabled': True,
#                                'rotation': -90,
#                                'color': '#FFFFFF',
#                                'align': 'right',
#                                'format': '{point.y}',
#                                 'y':10,
#                             'style': {
#                                     'fontSize': '13px',
#                              'fontFamily': 'Verdana, sans-serif'}})
# H.save_file('top10评分')



