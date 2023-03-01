
#电影发布数量与数量图表绘制；
import pymongo
from pyecharts.charts import Bar
from pyecharts import options as opts
import pyecharts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType


db =pymongo.MongoClient('localhost',27017)
douban = db['douban']
item_info = douban['top250']


#清洗TOP250评分数据排行；
year_list =[]
country_list = []
dict_list = {}
#提取mongodb数据；
for i in item_info.find():
    dict_list[i['name']] = float(i['star'])
    year_list.append(i['year'])
    country_list.append(i['country'])

year_dict={}
for i in year_list:
    year_dict[i] =year_dict.get(i,0)+1
print(year_dict)
tuple_year = sorted(year_dict.items(),key=lambda item:item[0])
print(tuple_year)
year_list1 = []
for j in range(len(tuple_year)):
    a = int(str(tuple_year[j][0]).strip('\n').strip('\xa0'))
    b =tuple_year[j][1]
    list1 = []
    list1.append(a)
    list1.append(b)
    year_list1.append(list1)
print(year_list1)




bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([a[0] for a in year_list1])
    .add_yaxis('上映电影部数', [a[1] for a in year_list1],category_gap="60%")
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="豆瓣top10电影上映与时间分布", subtitle="数据来源：www.douban.com"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值")]))
)
bar.render('a.html')