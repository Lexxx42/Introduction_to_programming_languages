# Сколько всего знаков * будет выведено после исполнения фрагмента программы:
i = 0
while i < 5:
    print('*') # 5
    if i % 2 == 0: # 6
        print('**')
    if i > 2: # 6
        print('***')
    i = i + 1 # total = 17