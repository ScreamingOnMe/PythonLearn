from bs4 import BeautifulSoup

html_file = open('444.html', 'r', encoding='utf-8')

html_handle = html_file.read()
soup = BeautifulSoup(html_handle, features="lxml")
title_lists = soup.select("._2rhmJa p")

for title_list in title_lists:
    print(title_list.string)
