""" This program generates a list of numbers and outputs a list of elements
of the original list whose values are greater than the previous element. """
# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint


def generate_list(list_len: int) -> list:
    """Function generating list of random numbers with a given length."""
    generated_list = [randint(0, 100) for _ in range(list_len)]
    print(generated_list)
    return generated_list


def filter_list(list_for_filter: list) -> list:
    """Function  creating filter list of
    the original list whose values are greater than the previous element."""
    answer_list = [list_for_filter[i] for i in range(1, len(list_for_filter)) if
                   list_for_filter[i] > list_for_filter[i - 1]]
    print(answer_list)
    return answer_list


def user_input() -> int:
    """Function of user input for list's length."""
    while True:
        try:
            number = int(input("Enter list's length: "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if number >= 1:
            return number
        print("Incorrect input! List's length must be greater than zero.")


def main() -> None:
    """Main program."""
    length_list = user_input()
    filter_list(generate_list(length_list))


if __name__ == '__main__':
    main()
