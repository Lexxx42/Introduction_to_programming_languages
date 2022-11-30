# conda поддерживает установку библиотек написанных на разных языках программирования
# conda install requests  # в терминале conda
import requests  # добавил через среду conda

r = requests.get('http://example.com')
print(r.text)

url = 'http://example.com'
par = {'key': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)  # Передача параметров в запрос
print(r.url)  # Сформированный url-адрес с учетом параметров GET запроса

# передача кук
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # Отправка сформированных cookies на сервер
print(r.text)

# принимаем куки от удаленного сервера
print(r.cookies['example_cookie_name'])
