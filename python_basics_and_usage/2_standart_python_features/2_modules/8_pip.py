# Установка утилиты pip
# Утилита pip позволит нам устанавливать пакеты из репозитория
# Python Package Index: https://pypi.python.org/pypi

# Если вы устанавливали python версии 3.4 или выше, то у вас уже должен быть установлен pip.

# Чтобы это проверить, вы можете запустить

# $ pip --version
# # или
# $ pip3 --version
# такая команда выведет текущую версию утилиты pip,
# а также папку, в которую будут устанавливаться пакеты.
# Убедитесь что в пути до данной папки, указана верная версия вашего интерпретатора.

# Если же не установлена (или путь до папки содержит другую версию интерпретатора),
# то вы можете перейти на сайт https://pip.pypa.io/en/latest/installing/
# и найти там инструкции по установке утилиты pip: а именно скачать с сайта файл get-pip.py,
# и запустить его с помощью своего интерпретатора python.
# Если у вас на операционной системе несколько интерпретаторов,
# то убедитесь, что вы запустили файл get-pip.py, используя правильный
# (интерпретатор языка python3 может называться, как python, так и python3,
# в зависимости от вашей операционной системы).

# Чтобы убедиться в том, что вы установили pip, попробуйте запустить инструкцию выше.

# Для того чтобы установить какую-нибудь библиотеку из Python Package Index
# (например пакет simple-crypt из следующей задачи), необходимо запустить команду

# $ pip install simple-crypt

# Если операционная система linux скажет, что вам не хватает прав для данной операции,
# используйте команду $ sudo pip install simple-crypt

# Утилита pip очень понадобится нам в третьем модуле для установки различных библиотек,
# поэтому если у вас возникла проблема с установкой данной утилиты,
# пожалуйста, напишите это в комментариях.

# Примечание:

# Самым успешным способом на данный момент установки данного пакета на windows,
# судя по комментариям, является установка дистрибутива Anaconda и дальнейшая
# установка пакетов с его помощью.
# Anaconda является хорошим дистрибутивом и вполне подойдет нам далее для прохождения курса.
