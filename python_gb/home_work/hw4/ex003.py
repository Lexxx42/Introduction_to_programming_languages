# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint


def user_input() -> None:
    input_number = int(input('Please enter a natural number N: '))
    if input_number > 0:
        generate_list(input_number)
    else:
        print('Please enter a number greater than zero')
        user_input()


def generate_list(length: int) -> list:
    generated_list = [randint(-9, 9) for _ in range(length)]
    print(generated_list)
    find_similar_items(generated_list)
    return generated_list


def find_similar_items(list_for_search) -> list:
    similar_elements = {}
    out_list = []
    count = 1
    for i in range(len(list_for_search)):
        if list_for_search[i] not in similar_elements:
            similar_elements[list_for_search[i]] = count
        else:
            similar_elements[list_for_search[i]] = similar_elements.get(list_for_search[i]) + 1
    for key in similar_elements:
        out_list.append(key)
    print(out_list)
    return out_list


def main() -> None:
    print('This program generates a list and outputs a list of non-repeating elements of the original sequence')
    user_input()


if __name__ == '__main__':
    main()
