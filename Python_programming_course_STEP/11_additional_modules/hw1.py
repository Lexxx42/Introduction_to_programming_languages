# Скачайте файл. В нём указан адрес другого файла,
# который нужно скачать с использованием модуля requests и посчитать число строк в нём.
#
# Используйте функцию get для получения файла
# (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
#
# После получения файла вы можете проверить результат,
# обратившись к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность.
# Для подсчёта количества строк разбейте текст с помощью метода splitlines.
#
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests

with open('dataset_3378_2.txt') as inf:  # закрывается самостоятельно
    text = inf.readline()
    text = text.strip()
    link_in_dataset = text

url = link_in_dataset  # get link or url
r = requests.get(url, allow_redirects=True)

open('stepic.txt', 'wb').write(r.content)  # Save the content with name

with open('stepic.txt') as inf:  # закрывается самостоятельно
    line_count = sum(1 for line in open('stepic.txt'))

print(line_count)
