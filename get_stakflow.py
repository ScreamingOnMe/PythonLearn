import requests

"""
# response = requests.get("https://stackoverflow.com/questions")
# soup = BeautifulSoup(response.text, "html.parser")
# questions = soup.select(".question-summary")
# for question in questions:
#    print(question.select_one(".question-hyperlink").getText())
# print(question.select_one(".vote-count-post").getText())
"""
from bs4 import BeautifulSoup

url = "https://www.jianshu.com/p/f7d7461a39d8"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response)
soup = BeautifulSoup(response.text, features="lxml")
title_lists = soup.select("._2rhmJa p")

title_aaa = soup.select("p")
print(title_aaa)
# print(title_aaa[0])

with open('test.txt', 'w') as f:

    for i in title_aaa:
        f.read()
        # print(i.string)

"""for title in title_aaa:
    print(title.string)"""


"""
标签内的<p>未处理掉，未解决
"""
"""for title_list in title_lists:
    print(title_list.string)
"""

"""
test in to github
"""
