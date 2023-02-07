# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е.
# внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C,
# что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

# Sample Input 1:

# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
# Sample Output 1:

# Yes
# Sample Input 2:

# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample1.html
# Sample Output 2:

# No
# Sample Input 3:

# https://stepic.org/media/attachments/lesson/24472/sample1.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
# Sample Output 3:

# Yes


# Time limit ((
import sys
import re
import urllib.request
from bs4 import BeautifulSoup

sys.stdin = open("hw4.txt")
# a, b = input().replace('stepic.org','stepik.org'), input().replace('stepic.org','stepik.org')
#
# html_page = urllib.request.urlopen(a)
# soup = BeautifulSoup(html_page, "html.parser")
# for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
#     html_page_inner = urllib.request.urlopen(link.get('href'))
#     soup_inner = BeautifulSoup(html_page_inner, "html.parser")
#     for link_inner in soup_inner.findAll('a', attrs={'href': re.compile("^https://")}):
#         if b in link_inner.get('href'):
#             print("Yes")
#         else:
#             print("No")


import requests
from lxml import html
import sys

a, b = input().replace('stepic.org', 'stepik.org'), input().replace('stepic.org', 'stepik.org')
res_a = requests.get(a)
if res_a.status_code != 200 or not res_a.text:
    print("No", end="")
    sys.exit()
list_links = []
html_1 = html.document_fromstring(res_a.text)


def func_1(list_1, ref_html):
    for item in ref_html.iter('a'):
        list_1.append(item.get('href').replace('stepic.org', 'stepik.org'))
    return list_1


list_1 = func_1(list_links, html_1)
for i, asd in enumerate(list_1):
    res_new = requests.get(list_1[i])
    if res_new.status_code != 200 or not res_new.text:
        continue

    items = []
    html_new = html.document_fromstring(res_new.text)

    for item_1 in html_new.iter('a'):
        items.append(item_1.get('href').replace('stepic.org', 'stepik.org'))
        if b in items:
            print("Yes", end="")
            sys.exit()
print("No", end="")

# import requests


# class Link_scanner:
#     def __init__(self, link_A, link_B):
#         self.__link_A = link_A
#         self.__link_B = link_B
#
#     @staticmethod
#     def link_list_gen(current_link: str) -> list[str]:
#         return [link for link in requests.get(current_link).text.split('"') if link.startswith("https:")]
#
#     def equals_link(self) -> str:
#         for link in self.link_list_gen(self.__link_A):
#             for link_inners in self.link_list_gen(link):
#                 if link_inners.replace('stepic.org', 'stepik.org') == self.__link_B:
#                     return "Yes"
#             return "No"
#
#
# answer = Link_scanner(input().replace('stepic.org', 'stepik.org'), input().replace('stepic.org', 'stepik.org'))
# print(answer.equals_link())


# import requests
# import re
#
#
# def get_urls(url: str) -> list:
#     urls = []
#     res = requests.get(url)
#     if res.status_code == 200:
#         string = res.text
#         pattern = r'href="(.+)"'
#         urls = re.findall(pattern, string)
#     return urls
#
#
# def search_url(url1: str, url2: str) -> str:
#     urls_in_page = get_urls(url1)
#
#     if not urls_in_page or url2.replace('stepik.org', 'stepic.org') in urls_in_page:
#         return 'No'
#
#     for ur in urls_in_page:
#         urls_in_page = get_urls(ur)
#         if url2.replace('stepik.org', 'stepic.org') in urls_in_page:
#             return 'Yes'
#
#
# url1, url2 = input().replace('stepic.org', 'stepik.org'), input().replace('stepic.org', 'stepik.org')
# print(search_url(url1, url2))
