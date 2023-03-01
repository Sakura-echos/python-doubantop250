import pymongo
from pyecharts.charts import Bar
from pyecharts import options as opts
import pyecharts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType


db =pymongo.MongoClient('localhost',27017)
douban = db['douban']
item_info = douban['top250']

daoyan_list = []
for i in item_info.find():
    print(i['daoyan'])
    if '/' in str(i['daoyan']):
        a = str(i['daoyan']).split('/')
        daoyan_list.append(a[0])
        daoyan_list.append(a[1])
    else:
        daoyan_list.append(i['daoyan'])
daoyan_list1 = list(set(daoyan_list))
count_list =[]
daoyan_dict ={}
for i in daoyan_list1:
    count_list.append(daoyan_list.count(i))
    daoyan_dict[str(i).strip(' ')] =daoyan_list.count(i)
print(count_list)
print(daoyan_dict)
daoyan_dict1 = sorted(daoyan_dict.items(),key=lambda item:item[1],reverse=True)
print(daoyan_dict1)
daoyan_list2 = []
count_list2 =[]
for i in daoyan_dict1:
    daoyan_list2.append(i[0])
    count_list2.append(i[1])

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT ,width='900px',height='600px'))
    .add_xaxis([a for a in daoyan_list2[:15]])
    .add_yaxis('导演作品数量', [a for a in count_list2[:15]],category_gap='60%',color=range(1,10))
    .set_series_opts(label_opts=opts.LabelOpts(font_size=12))
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60,font_size=12,)),title_opts=opts.TitleOpts(title="top250电影中导演作品数量top10", subtitle="数据来源：www.douban.com"))

)
bar.render('top10导演.html')
