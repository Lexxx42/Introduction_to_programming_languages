with open('input_data.txt') as inf:  # закрывается самостоятельно
    text = ''
    for line in inf:
        line = line.strip()
        text += line + ' '
    text = text.lower()
    list_1 = list(text)
    print()

