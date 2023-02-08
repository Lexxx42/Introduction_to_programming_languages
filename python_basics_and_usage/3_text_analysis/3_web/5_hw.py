# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов.
# То есть, это последовательность символов, которая следует сразу после символов протокола,
# если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида

# <a href="../some_path/index.html">.

# Сайты следует выводить в алфавитном порядке.

# Пример HTML файла:

# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">

# Пример ответа:

# mail.ru
# neerc.ifmo.ru
# stepic.org
# www.ya.ru
# ya.ru

# import requests
# import lxml.html
import tldextract

#
# list_links = set()
# link = requests.get(input().strip().replace('stepic.org', 'stepik.org'))
# html_1 = lxml.html.document_fromstring(link.text)
#
# for a in html_1.iter('a'):
#     list_links.add(a.get('href'))
# list_links.remove(None)
#
# answer = set()
# for link in list_links:
#     ext = tldextract.extract(link)
#     if ext.domain:
#         answer.add('.'.join(ext) if ext.subdomain else '.'.join(ext[1:]))
#
# for item in sorted(answer):
#     print(item)


# import requests
# import re
#
# #link = input().strip().replace('stepic.org', 'stepik.org')
# #file = requests.get(link).text
file = r'''<a href="https://stepic.org/media/attachments/lesson/24472/sample1.html">1</a>
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib">
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
<a href="../some_path/index.html">
<a href="sas-_0123d.ifmo.ru">
<a target='_top' href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">'''
# print(*sorted(set(re.findall(r'<a[^>]* href=[\"\'](\w*w*.?\w+.\w+)[\"\']', file))), sep='\n')
#
# # a = set(re.findall(r'<a[^>]* href="([^"\']*)"', file))
# # b = set()
# # for item in a:
# #     b.add((li if len(li := re.findall(r'\S+://([^/]+)/\S+', item)) == 1 else ["+"])[0])
# # b.remove("+")
# # for item in sorted(b):
# #     print(item)

import requests
import re

# link = input().strip().replace('stepic.org', 'stepik.org')

# file = requests.get(link).text
a = set(re.findall(r'<a[^>]* href="([^"\']*)"', file))
print(a)
b = set()
for item in a:
    b.add((li if len(li := re.findall(r'', item)) == 1 else ["+"])[0])
b.remove("+")
for item in sorted(b):
    print(item)
