# Slicing
dna = 'ATTCGGAGCT'
print(dna[1])  # T
print(dna[1:4])  # TTC
print(dna[:4])  # ATTC
print(dna[4:])  # GGAGCT
print(dna[-4:])  # AGCT
print(dna[1:-1])  # TTCGGAGC
print(dna[1:-1:2])  # TCGG от:до:шаг
print(dna[::-1])  # TCGAGGCTA (сиволы в обратном порядке) отрицательный шаг


# Задача - палиндром
# Дана геномная последовательность.
# Проверить, является ли она палиндромом.
# Строка является палиндромом, если читается в обоих направлениях одинаково.

# Входные данные 1: CAGGTGGAC 
# выходные данные 1: YES
# Входные данные 2: GATTACA
# выходные данные 2: NO

s = input()
i=0
j=len(s)-1
is_palindrom = True
while i<j:
    if s[i] != s[j]:
        is_palindrom=False
        break
    i+=1
    j-=1
    if is_palindrom:
        print('YES')
    else:
        print('NO')


s = input() # минус - занимаем много памяти
if s==s[::-1]:
    print('YES')
else:
    print('NO')
