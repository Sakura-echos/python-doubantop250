import requests
from bs4 import BeautifulSoup
import time
import pymongo


from pyecharts import options as opts
from pyecharts.charts import Page, Pie


# headers={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
#     'Cookie': 'douban-fav-remind=1; bid=xV3mzxZaZxE; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1558577880%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DV45iHCRmrzprwRNYFC4Tj2b6lo3J1MbSYFIzkgsyd9EERM6EE6OIaTGDe9z7NaJj%26wd%3D%26eqid%3Db8eae7580058b189000000025ce602d1%22%5D; _pk_id.100001.4cf6=cf9fd67f-eed2-4398-a10d-333daee6b8b7.1558577880.1.1558577880.1558577880.; _pk_ses.100001.4cf6=*; __utma=30149280.1353623796.1524120262.1556333363.1558577881.8; __utmb=30149280.0.10.1558577881; __utmc=30149280; __utmz=30149280.1558577881.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2144420921.1558577881.1558577881.1558577881.1; __utmb=223695111.0.10.1558577881; __utmc=223695111; __utmz=223695111.1558577881.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
# }
db =pymongo.MongoClient('localhost',27017)
douban = db['douban1']
item_info = douban['top2501']
'''
    重新爬取country列表；
'''
# for i in range(0, 10):
#     num = str(i * 25)
#     url = 'https://movie.douban.com/top250?start={}&filter='.format(num)
#     time.sleep(2)
#
#     soup = requests.get(url,headers=headers)
#     response = BeautifulSoup(soup.text,'lxml')
#     lists = response.select('div.info')
#     for list in lists:
#         type_list = list.select('div.bd p')[0].text.strip('').split('...')[-1].split('/')
#         country = type_list[1].split(' ')
#         data ={'country':country}
#         item_info.insert_one(data)
"""
        构建top250电影中出自国家最多的20个国家的列表；
"""
country_list =[]
for i in item_info.find():
    if '导' not in i['country']:
        for j in i['country']:
            if j !='':
                country_list.append(str(j).strip('\xa0'))

country_list1 = list(set(country_list))
append_list=[]
for i in country_list1:
    list11 =[]
    list11.append(str(i))
    list11.append(country_list.count(i))
    append_list.append(list11)
list22 = sorted(append_list,key =lambda d:d[1],reverse=True)[:10]


c = (Pie().add("",
            [list(z) for z in zip(list(a[0] for a in list22),list(a[1] for a in list22) )],
            center=["35%", "50%"])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="豆瓣top250电影产源国家数量占比"),
            legend_opts=opts.LegendOpts(pos_bottom='0'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
c.render('country.html')

