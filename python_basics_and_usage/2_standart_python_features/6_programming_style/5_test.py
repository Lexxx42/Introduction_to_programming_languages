# Какие способы слайсинга списка являются допустимыми с точки зрения рекомендаций PEP 8?

# Примечание: доверяй, да проверяй:
# сообщения чекера pycharm и стандартной утилиты pep8,
# может отличаться от рекомендаций официального документа PEP 8 :)

# a[lower + offset : upper + offset] <-
# a[lower + offset:upper + offset] - BAD!
# a[lower+offset : upper+offset] <-
# a[lower : : upper] - BAD!
# a[lower:upper], a[lower:upper:], a[lower::step] <-
