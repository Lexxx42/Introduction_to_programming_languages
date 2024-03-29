# Когда мы говорим о поиске информации в каком-либо тексте то мне прежде всего в голову приходит интернет.
# Потому что это первое место куда я иду, когда мне нужно найти какую-либо информацию.

# В данном уроке мы с вами поговорим о том, как устроен интернет, http-запросах и о html-страницах.

# Вообще в интернете существует различное количество протоколов для передачи различной информации.
# Есть протоколы для обмена файлами, почтой.

# Но мы с вами будем говорить про http, т.е. протокол обмена гипертекстом.

# Гипертекст достаточно старый.
# Базовая концепция, которая легла в основу гипертекста - это гиперссылки.
# По сути, гипертекст -- это текстовый документ, который содержит в себе также ссылки на другие
# текстовые документы.

# Например, если вы откроете статью на википедии, то вы наверняка можете быть любопытны и
# можете перейти на пару статей, которые связаны с той, которую вы уже читаете.

# И именно эта очень старая концепция легла в основу того интернета, который мы знаем.

# Что же такое http протокол?

# Прежде всего, у нас будет две стороны, которые участвуют в общении.

# Первая сторона -- клиент.
# Это мы с вами, пользователи интернета.

# А вторая сторона -- это сервер, к которому мы делаем запрос.

# Т.е. мы будем запрашивать у сервера какой-нибудь ресурс.
# Что же может быть ресурсом?

# Ресурс, прежде всего, веб страница или какие-нибудь файлы.

# Ресурсы мы описываем в интернете используя URL.

# URL - universal resource locator, единообразный локатор ресурса.

# Как и где мы можем данный ресурс.

# URL: протокол (https), домен, хост (//stepic.org), путь до ресурса (/512).

# Мы написали URL используя три основные компонента.
# Однако важно помнить, что бывают еще и другие.

# Первая компонента -- это протокол.

# Можно явно указывать протокол, по которому мы получаем данный ресурс.
# Потому что протоколы обмена информации в интернете отличаются друг от друга.
# Например, протоколы обмена гипертекстом сильно отличаются от протокола обмена файлами ftp.

# Вторая компонента -- это домен.

# Важно понимать, что в сети интернет очень много серверов.
# Домен нужен, прежде всего, чтобы распознать, на какой из этих компьютеров-серверов нам необходимо
# отправить наш запрос.

# Третья компонента.

# Может оказаться, что на нашем сервере очень много ресурсов.
# И нам необходимо показать какой именно из всех ресурсов на сервере нам нужен.
# Для этого мы используем путь.

# Давайте вернемся к http.

# Как клиент и сервер обмениваются сообщениями?

# http -- является текстовым протоколом.
# Поэтому сначала клиент посылает запрос в текстовом формате в определенном виде.
# А затем к нему приходит ответ в текстовом формате.

# Запрос / Request

# GET /wiki/Python HTTP/1.1
# GET - метод, который мы хотим применить к нашему ресурсу.
# Метод GET означает, что мы хотим получить страницу на ресурс /wiki/Python, который
# находится на домене ru.wikipedia.org

# /wiki/Python - ресурс, который мы хотим получить внутри Википедии.

# HTTP/1.1 - версия протокола.

# В данный момент http протокол используется не только для обмена текстовой информации,
# с помощью него вы можете загружать картинки, музыку и даже видеозаписи.

# В http протоколе объявлено несколько методов и самый популярно используемый метод - GET.

# GET используется для того, чтобы мы получили данный ресурс.
# Если ресурс является веб-станицей, то с помощью GET мы получим код данной html страницы.
# Если запрашиваем картинку, то мы получим бинарные данные данной картинки.
# Чаще всего метод GET не изменяет сами данные, которые хранятся на сервере.

# А метод POST для этого предназначен.
# Чаще всего, когда мы используем метод POST мы меняем те или иные данные, которые связаны
# с теми ресурсами, которые мы запрашиваем.
# Например, формы смены пароля, когда вы их заполняете и нажимаете enter.

# В http есть и другие методы, однако эти два самые используемые.

# Также в запросе может быть некоторое число заголовков, которые
# разделены точкой.

# Host: ru.wikipedia.org

# Заголовок: домен.

# Ответ на наш запрос возвращается нам в похожем формате.

# HTTP/1.1 200 OK
# Версия http, статус код, сообщение

# В нашем случае статус 200 - все прошло хорошо.

# Статусные коды бывают разные.
# 200 - успешно загрузили данную страницу.
# 404 - данный ресурс не был найден на сервере.
# Если произошла серверная ошибка при обработке вашего запроса - 500.

# После первой строки, идет несколько заголовков:
# Дата
# Тип контента - что за содержимое мы запрашиваем.

# После того как заканчиваются заголовки идет пустая строка.

# После которой и следует запрашиваемый ресурс.

# Таким образом http протокол достаточно простой.
# Мы в текстовом формате, указываем информацию о ресурсе.
# Он сначала показывает статус-код и показывает гладко ли все прошло.
# Затем немного служебной информации, после чего сам ресурс, который мы запрашивали.
