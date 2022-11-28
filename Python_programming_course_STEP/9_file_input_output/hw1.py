with open('dataset_3363_2.txt') as inf:  # закрывается самостоятельно
    text = inf.readline()
    text = text.strip()
    keys = []
    digits = []
    digit = ''
    for i in range(len(text)):
        if text[i].isalpha():
            keys.append(text[i])
        if text[i].isdigit():
            if text[i-1].isdigit():
                continue
            digit += text[i]
            if i < len(text)-1:
                if text[i+1].isdigit():
                    digit += text[i+1]
            digits.append(int(digit))
            digit = ''
    for j in range(len(keys)):
        print(f'{keys[j]*digits[j]}', end='')
