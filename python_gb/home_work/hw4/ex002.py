# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from eratosthenes import eratosthenes


def prime_factors(input_number: int):
    factors = []
    if input_number > 1:
        prime_list = eratosthenes(input_number)
        i = 0
        while input_number != 1 or input_number == 0:
            if input_number % prime_list[i] == 0:
                factors.append(prime_list[i])
                input_number /= prime_list[i]
            else:
                i += 1
        print(factors)
    else:
        print('Natural number must be positive and greater than 1.')
        user_input()
    return factors


def user_input():
    input_number = int(input('Please enter a natural number N: '))
    if input_number > 0:
        prime_factors(input_number)
    else:
        print('Number must be natural (greater than 0)')
        user_input()


def main():
    print('This program lists the prime factors of N.')
    user_input()


if __name__ == '__main__':
    main()
