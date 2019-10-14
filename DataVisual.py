import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
import pandas as pd

df = pd.read_excel(r'tables/data_pts.xlsx')

def points():
    pts = np.zeros(len(df['coin']))
    view_c = 0.025
    share_c = 3
    coin_c = 1
    fav_c = 1
    for i in range(len(df['coin'])):
        if i%100000==0:
            print(i)
        reviseA = 1
        reviseB = min(1, (share_c*df.share[i]+fav_c*df.favorite[i]+coin_c*df.coin[i])\
                    /(view_c*df.viewcount[i]+share_c*df.share[i]+coin_c*df.coin[i]))
        pts[i] = view_c*df.viewcount[i]*reviseA + (share_c*df.share[i]+coin_c*df.coin[i])*reviseB + fav_c*df.favorite[i]
    df['pts'] = pts

def keyword_remove():
    STR1 = df.keywords[5][-28:]
    STR2 = df.keywords[2][-34:]
    STR3 = df.keywords[7][-28:]
    STR4 = df.keywords[854][-28:]
    newkeyword = np.empty(len(df['coin']))

    for i in range(len(df['coin'])):
        key = df.keywords[i][-28:]
        if key!=STR1 and df.keywords[i][-34:]!=STR2 and key!=STR3 and key!=STR4:
            print(i, df.av[i], df.keywords[i], df.keywords[i][0:28])
            if df.duration[i]==0:
                print('success.')


time = df.uploadtime
from datetime import datetime
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2009, 7, 13)
end_date = date(2019, 5, 1)
view = []
view_total = []
acc_total = []
acc = []
authorlist = []
i = 0
total = 0
days_total = 0
name = "全明星"
iteratior = df.pts
for single_date in daterange(start_date, end_date):
    today = 0
    days = 0
    #print(df.uploadtime[i].timestamp())
    for s in range(i, len(iteratior)):
        #print(single_date, df.uploadtime[len(df.viewcount) - i - 1].to_pydatetime().date())
        if single_date == df.uploadtime[len(iteratior) - i - 1].to_pydatetime().date():
            #print(df.keywords[len(iteratior) - i - 1])
            #if name in df.keywords[len(iteratior) - i - 1]:
            #if df.authorid[len(iteratior) - i - 1] not in authorlist:
            if authorlist.append(df.authorid[len(iteratior) - i - 1])
                today += 1#iteratior[len(iteratior) - i - 1]
            days += iteratior[len(iteratior) - i - 1]
            i+=1

        else:
            break
    total += today
    days_total += days
    view += [today]
    acc += [total]
    view_total += [days]
    acc_total += [days_total]
#timestamp = datetime.timestamp(now)
#print("timestamp =", timestamp)

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')


from scipy.signal import lfilter

import datetime
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
date1 = datetime.date(2009, 7, 13)
date2 = datetime.date(2019, 5, 1)
delta = datetime.timedelta(days=1)

dates = drange(date1, date2, delta)

n = 30  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
newview = [x / (y+1) for x,y in zip(view,view_total)]
yy = lfilter(b,a,view)
plt.plot_date(dates, yy, linewidth=1, c="r",fmt='-')
ax2 = plt.twinx()
ax2.plot_date(dates, acc, linewidth=1, c="b",fmt='-')
#plt.plot(yy, linewidth=1, c="b")  # smooth by filter
ax2.set_ylabel('new video uploader')
#plt.ylabel('new video per day')
plt.savefig('view.jpg')
plt.show()