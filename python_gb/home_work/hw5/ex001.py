# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: -1
#
# out
# The data is incorrect
from random import shuffle


def create_random_words_fixed_length(alphabet_in: str, words_quantity: int) -> tuple[list[str], list[str]]:
    if words_quantity <= 0:
        print('The data is incorrect')
        exit()

    alphabet_list = list(alphabet_in)
    output_list = []

    for _ in range(words_quantity):
        shuffle(alphabet_list)
        output_list.append(''.join(([x for x in alphabet_list])))

    result = list(filter(lambda x: x != 'абв', output_list))
    return output_list, result


def list_into_strings(list_1: list, list_2: list) -> None:
    in_string = ''
    out_string = ''
    for _ in list_1:
        in_string = ' '.join(list_1)
    print(in_string)

    for _ in list_2:
        out_string = ' '.join(list_2)
    print(out_string)


def main() -> None:
    print('This program removes all words containing "абв" from the text.'
          ' The default words are generated from the "абв" dictionary.')
    alphabet = 'авб'
    number_of_words = int(input('Number of words: '))
    in_list, out_list = create_random_words_fixed_length(alphabet, number_of_words)
    list_into_strings(in_list, out_list)


if __name__ == '__main__':
    main()
