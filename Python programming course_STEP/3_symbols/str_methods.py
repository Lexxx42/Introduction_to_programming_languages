s = 'aTGcc'
p = 'cc'
print(s.upper())  # ATGCC
print(s.lower())  # atgcc
print(s.count(p))  # 1 - сколько раз p встречается в s рассматриваются только не перекрывающиеся вхождения
print(s.find(p))  # 3 - первое вхождение (индекс) p в s
print(s.find('A'))  # -1 строка 'A' не входит в s
# Проверка вхождения в строку: if 'TG' in s: ...
print(s.replace('c', 'C'))  # aTGCC - заменяем все вхождения 'c' на 'C'

# Последовательные вызовы методов
s = 'agTtxAGtc'
print()
print(s)
print(s.upper().count('gt'.upper()))
