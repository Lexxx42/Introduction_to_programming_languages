# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество dd известных нам слов,
# после чего на d строках указываются эти слова.
# Затем передаётся количество l строк текста для проверки, после чего l строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# Sample Input:
#
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
# Sample Output:
#
# stepic
# champignons
# the


def input_known_words(number_of_words):
    known_words = set()
    for c in range(number_of_words):
        known_words.add(input().lower())
    return known_words


def input_check_words(number_of_words):
    check_words = set()
    for i in range(number_of_words):
        line_check = input().lower().split()
        for j in line_check:
            check_words.add(j)
    return check_words


number_of_known_words = int(input())
dict_known_words = input_known_words(number_of_known_words)
number_of_words_for_check = int(input())
dict_check_words = input_check_words(number_of_words_for_check)
dl = dict_check_words.difference(dict_known_words)
for i in dl:
    print(i)
