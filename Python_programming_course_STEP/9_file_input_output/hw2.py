with open('dataset_3363_3.txt') as inf:  # закрывается самостоятельно
    text = ''
    for line in inf:
        line = line.strip()
        text += line + ' '
    text = text.lower()
    list_1 = text.split(' ')
    dict_answer = {list_1[0]: 0}
    for i in range(len(list_1)):
        dict_answer[list_1[i]] = 0
    for i in range(len(list_1)):
        dict_answer[list_1[i]] = dict_answer.get(list_1[i]) + 1
    key_max = ''
    val_max = 0
    for key, value in dict_answer.items():
        if value > val_max:
            key_max = key
            val_max = value
        else:
            continue
    print(key_max, val_max)
