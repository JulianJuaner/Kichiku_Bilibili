import lxml, lxml.html
from lxml import etree
from multiprocessing import Pool as ThreadPool
from datetime import datetime
import requests
import time
import sys
import re
import json
import MySQLdb
import numpy as np


urls = []

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

time1 = time.time()
#video_counter = 547653
#48010
b = np.load("3dMAD.npy")
print(len(b))
index = 0
for k in range(0, len(b)):
    if int(b[k]) == 2729400:
        index = k
        break
for i in range(k, len(b)):
    #if b[i]>17000000:
        #continue
    url = 'https://api.bilibili.com/x/web-interface/view?aid=' + str(int(b[i]))
    #print(b[i])
    urls.append(url)
print('url loaded.')
#'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
Validtid = [26, 119, 126, 127, 22]
print("sleeping")
#time.sleep(500)
print("over")
retry = False
Validtype = ['2dMAD', 'kichiku', 'VOCALOID', 'guide', '3dMAD']
try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='zhangyc', port=3306, charset='utf8')
    cur = conn.cursor()
    conn.select_db('bilibili')
except Exception as e:
    print(e)

def spider(url):
    print(url)
    global retry
    try:
        JSON = requests.get(url, headers = head, timeout=(10, 10)).text
    except Exception as e:
        print(e)
        if retry == False:
            spider(url)
            retry = True
            return
        return

    retry = False

    JSON = json.loads(JSON)
    #print(json.dumps(JSON, indent=4, ensure_ascii=False))
    #time.sleep(0.13)
    #print(url)
    if JSON["code"] == 0:
        #video_counter += 1
        #print(video_counter, end='')
        content = JSON["data"]
        if content["tid"] not in Validtid:
            return
        else:
            #print(url)
            #time.sleep(0.02)
            av = content["aid"]
            title = content["title"]
            videotype = Validtype[Validtid.index(content["tid"])]
            uploadDate = datetime.fromtimestamp(content["pubdate"])
            description = content["desc"]
            duration = content["duration"]
            authorid = content["owner"]["mid"]
            authorname = content["owner"]["name"]
            stat = content["stat"]
            viewcount = stat["view"]
            danmaku = stat["danmaku"]
            comment = stat["reply"]
            favorite = stat["favorite"]
            coin = stat["coin"]
            share = stat["share"]
            likes = stat["like"] 

            #print(av, title, videotype, uploadDate)
            #print(description)
            #print(authorid, authorname, duration)
            #print(viewcount, danmaku, comment, favorite, coin, share, likes)

            
            htmlKey = "https://www.bilibili.com/video/av" + str(av)

            try:
                html = requests.get(htmlKey, headers = head, timeout=(10, 10))

            except Exception as e:
                print(e)
                if retry == False:
                    spider(url)
                    retry = True
                    return
                return
            retry = False

            selector = etree.HTML(html.text)
            content = selector.xpath("//html")[0]
            try:
                keywords = content.xpath('//head/meta[@itemprop="keywords"]/@content')[0]
            except Exception as e:
                print(e)
                spider(url)
                return

            #print(keywords)
            cur.execute('INSERT INTO kichu_video(av, title, videotype, uploadtime, description,\
                                    authorid, authorname, duration,\
                                    viewcount, danmaku, comment, favorite, coin, share, likes, keywords)\
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                    (av, title, videotype, uploadDate, description,\
                                    authorid, authorname, duration,\
                                    viewcount, danmaku, comment, favorite, coin, share, likes, keywords))

            print ("Succeed: av" + str(av))


#pool = ThreadPool()
# results = pool.map(spider, urls)
#print('here!')
for m in urls:
    spider(m)
    #print('here!')

