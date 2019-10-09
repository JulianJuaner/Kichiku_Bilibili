import lxml, lxml.html
from lxml import etree
from multiprocessing import Pool as ThreadPool
from datetime import datetime
import requests
import time
import sys
import re
import json
import pymysql
import pandas as pd

urls = []

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

time1 = time.time()
#time.sleep(7200)
#video_counter = 547653
#48010
number = 0
data = pd.read_csv('./tables/popup_fan.csv')
data_id = data.iloc[:,0]
print(len(data_id))

for i in data_id:
    url = ' https://api.bilibili.com/x/web-interface/card?mid=' + str(i) + '&;jsonp=jsonp&article=true'
   
    
    urls.append(url)
print('url loaded.')
#'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
Validtid = [26, 119, 126, 127, 22]

retry = False
Validtype = ['2dMAD', 'kichiku', 'VOCALOID', 'guide', '3dMAD']
fanslist = []
def spider(url):
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
    time.sleep(0.3)
    #print(url)
    if JSON["code"] == 0:
        #video_counter += 1
        #print(video_counter, end='')
        content = JSON["data"]
        print(url)
        #time.sleep(0.02)
        fans = content["archive_count"]
        print(fans)
        print("----------",number*100/len(data_id),"%","----------")
        fanslist.append(fans)
                
       

#pool = ThreadPool()
# results = pool.map(spider, urls)
#print('here!')
for m in urls:
    number+=1
    spider(m)
    #print('here!')

df = pd.DataFrame(fanslist)
df_csv = pd.read_csv('./tables/popup_fan.csv')
df_csv['tot_num'] = df
df_csv.to_csv('./tables/popup_fan.csv', index=False, mode= 'w')
