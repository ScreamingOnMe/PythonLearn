import requests
from bs4 import BeautifulSoup

url = "https://guba.eastmoney.com/list,600289.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
title_lists = soup.select('.articleh a')
title_cut = title_lists[::2]  # 用步长判断列表，0,2,4,6 偶数的有title属性
for i in title_cut:
    print(f"股吧标题:", i.string)
