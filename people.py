import pymongo
from pyecharts.charts import Bar
from pyecharts import options as opts
import pyecharts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

quote = ''
db =pymongo.MongoClient('localhost',27017)
douban = db['douban']
item_info = douban['top250']


num_list =[]
for i in item_info.find():
    list1 =[]
    list1.append(str(i['name']))
    list1.append(int(i['people_num']))
    num_list.append(list1)
    quote =quote+str(i['quote']).strip('\n').strip(' ')
print(quote)
print(sorted(num_list,key = lambda d:d[1],reverse=True))
num_list1 =sorted(num_list,key = lambda d:d[1],reverse=True)

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([a[0] for a in num_list1[:20]],)
    .add_yaxis('观看人数', [a[1] for a in num_list1[:20]],category_gap="60%")

    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60,font_size=12,)),title_opts=opts.TitleOpts(title="豆瓣评价人数top20电影", subtitle="数据来源：www.douban.com"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值")]))
)
bar.render('people.html')

