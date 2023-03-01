import requests
from bs4 import BeautifulSoup
import time
import pymongo

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    'Cookie': 'douban-fav-remind=1; bid=xV3mzxZaZxE; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1558577880%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DV45iHCRmrzprwRNYFC4Tj2b6lo3J1MbSYFIzkgsyd9EERM6EE6OIaTGDe9z7NaJj%26wd%3D%26eqid%3Db8eae7580058b189000000025ce602d1%22%5D; _pk_id.100001.4cf6=cf9fd67f-eed2-4398-a10d-333daee6b8b7.1558577880.1.1558577880.1558577880.; _pk_ses.100001.4cf6=*; __utma=30149280.1353623796.1524120262.1556333363.1558577881.8; __utmb=30149280.0.10.1558577881; __utmc=30149280; __utmz=30149280.1558577881.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2144420921.1558577881.1558577881.1558577881.1; __utmb=223695111.0.10.1558577881; __utmc=223695111; __utmz=223695111.1558577881.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
}

db = pymongo.MongoClient('localhost',27017)
client = db['douban']
movie_list = client['top250']

'''
        抓取top250电影的上映时间、国家、评分、类型、评价人数；
'''
def get_movie_list(url,headers):
    soup = requests.get(url,headers=headers)
    response = BeautifulSoup(soup.text,'lxml')
    lists = response.select('div.info')
    for list in lists:

        sing_url =list.select('a')[0].get('href')
        name =list.select('div.hd .title')[0].text
        type_list = list.select('div.bd p')[0].text.strip('').split('...')[-1].replace(' ','').split('/')
        year =type_list[0]
        country = type_list[1]
        category = type_list[2]
        star = list.select('div.bd .star .rating_num')[0].text.replace(' ','')
        quote =list.select('div.bd .quote')[0].text
        people_num = list.select('div.bd .star span:nth-of-type(4)')[0].text.split('人')[0]
        get_detail_movie(sing_url,name,year,country,category,star,quote,people_num,headers)


'''
        抓取top250电影的执导导演、参演演员；并保存数据到mongodb中
'''

def get_detail_movie(movie_url,name,year,country,category,star,quote,people_num,headers):
    response = requests.get(movie_url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    daoyan =soup.select('#info > span:nth-of-type(1) > span.attrs')[0].text
    yanyuan =[]
    for i in soup.select('#info > span.actor > span.attrs'):
        yanyuan.append(i.text.replace('/',''))

    list1 =str(yanyuan).replace('[','').replace("'",'').split(' ')
    yanyuan = list1
    data ={'name':name,
           'year':year,
           'country':country,
           'category':category,
           'star':star,
           'quote':quote,
           'people_num':people_num,
           'daoyan':daoyan,
           'yanyuan':yanyuan
           }
    print(data)
    if movie_list.find_one({'name':name}):
        if '导' in year:
            if '中国大陆' in country:
                print('inserted failed')
    else:
        movie_list.insert_one(data)

'''
        构建递归循环；逐页爬取；
'''
if __name__ =='__main__':
    for i in range(0,10):
        num = str(i*25)
        url = 'https://movie.douban.com/top250?start={}&filter='.format(num)
        time.sleep(2)
        get_movie_list(url,headers)
