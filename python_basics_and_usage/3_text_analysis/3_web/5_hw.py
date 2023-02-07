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

import requests
import lxml.html
import tldextract

list_links = set()
link = requests.get(input().strip().replace('stepic.org', 'stepik.org'))
html_1 = lxml.html.document_fromstring(link.text)

for a in html_1.iter('a'):
    list_links.add(a.get('href'))
list_links.remove(None)

print(list_links)
answer = set()
for link in list_links:
    ext = tldextract.extract(link)
    if ext.domain:
        answer.add('.'.join(ext) if ext.subdomain else '.'.join(ext[1:]))

for item in sorted(answer):
    print(item)
