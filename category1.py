import pymongo
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

db =pymongo.MongoClient('localhost',27017)
douban = db['douban']
item_info = douban['top250']
category_list=[]
for i in item_info.find():
    a = str(i['category']).strip('\n').strip(' ')
    category_list.append(a)
    print(str(i['category']).strip('\n').strip(' '))
list1 =['爱情','犯罪','惊悚','动画','科幻','战争','喜剧','动作']
count_list =[]
for j in range(0,8):
    count = 0
    for i in category_list:
        if str(list1[j]) in i:
            count +=1
    count_list.append(count)

c = (Pie().add("",
            [list(z) for z in zip(list1, count_list)],
            center=["35%", "50%"])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="豆瓣top250电影类型数量占比"),
            legend_opts=opts.LegendOpts(pos_bottom='0'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
c.render('category.html')