import pymongo
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page

db =pymongo.MongoClient('localhost',27017)
douban = db['douban']
item_info = douban['top250']

yanyuan_list =[]

for i in item_info.find():
    if  '韩国' in str(i['country']).strip('\xa0'):
        print(i)
    for j in i['yanyuan']:
        if j != '':
            yanyuan_list.append(j)


yanyuan_list1 =list(set(yanyuan_list))
cbind_list =[]
for i in yanyuan_list1:
    a=[]
    a.append(i)
    a.append(yanyuan_list.count(i))
    cbind_list.append(a)

x = sorted(cbind_list,key=lambda d:d[1],reverse=True)
list11 =list(i[0] for i in x)[:20]
list22 =list(i[1] for i in x)[:20]
print(sorted(cbind_list,key=lambda d:d[1],reverse=True))

graph =(
           Funnel(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(
            "",
            [list(z) for z in zip(list11, list22)],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
       
        .set_global_opts(title_opts=opts.TitleOpts(title="优秀演员参演作品数量",pos_bottom=0))
    )
graph.render('yanyuan.html')