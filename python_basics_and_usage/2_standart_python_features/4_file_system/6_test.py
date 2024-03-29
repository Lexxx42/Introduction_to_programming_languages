# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

# Вам необходимо распаковать этот архив,
# и затем найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py".

# Ответом на данную задачу будет являться файл со списком таких директорий,
# отсортированных в лексикографическом порядке.

# Для лучшего понимания формата задачи, ознакомьтесь с примером.
# Пример архива
# Пример ответа

import os.path

os.chdir("sample")
answer = set()
for current_dir, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            answer.add(current_dir[2:])
print(output := "\n".join(sorted(answer)))

os.chdir("..")
with open("out_file.txt", "w", encoding="utf-8") as out_file:
    out_file.write(output)
