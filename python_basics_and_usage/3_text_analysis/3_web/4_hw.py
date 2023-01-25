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
# a, b = input().strip(), input().strip()

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

a, b = input(), input()
res_a = requests.get(a)
list_links = []

html = html.document_fromstring(res_a.text)
for a in html.iter('a'):
    list_links.append(a.get('href'))
    if b in list_links:
        print("Yes", end="")
        break
    else:
        print("No", end="")
