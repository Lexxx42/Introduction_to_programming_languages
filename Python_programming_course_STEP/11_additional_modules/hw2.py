# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

import requests


def readfile(file_name):
    with open(file_name) as inf:  # закрывается самостоятельно
        text = inf.readline()
        text = text.strip()
        link_in_dataset = text
        url = link_in_dataset  # get link or url
        r = requests.get(url, allow_redirects=True)
        open('stepic2.txt', 'wb').write(r.content)
        next_file()


def next_file():
    with open('stepic2.txt') as inf:  # закрывается самостоятельно
        text = inf.readline()
        text = text.strip()
        print(text)
        if "We" in text:
            print(text)
            for line in inf:
                line = line.strip()
                print(line)
            return
        link_in_dataset = 'https://stepic.org/media/attachments/course67/3.6.3/' + text
    url = link_in_dataset  # get link or url
    r = requests.get(url, allow_redirects=True)
    open('stepic2.txt', 'wb').write(r.content)
    next_file()


readfile('dataset_3378_3.txt')
