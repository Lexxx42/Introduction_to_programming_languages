""" This program for numbers between 20 and N finds multiples of 20 or 21. """


# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in
# 424
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126,
# 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240,
# 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357,
# 360, 378, 380, 399, 400, 420]


def user_input() -> int:
    """Function of user input for list's length."""
    while True:
        try:
            number = int(input("Enter N : "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if number >= 21:
            return number
        print("Incorrect input! N must be greater than 20")


def filter_input_list(value: int) -> list:
    """Function generating list of elements multiples of 20 or 21."""
    list_input = list(range(20, value + 1))
    filtered_list = list(filter(lambda x: not x % 20 or not x % 21, list_input))
    print(filtered_list)
    return filtered_list


def main() -> None:
    """Main program."""
    number_n = user_input()
    filter_input_list(number_n)


if __name__ == '__main__':
    main()
