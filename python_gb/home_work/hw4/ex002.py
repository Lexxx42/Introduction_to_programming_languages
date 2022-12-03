# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from eratosthenes import eratosthenes


def prime_factors(input_number):
    factors = set()
    if input_number > 1:
        prime_list = eratosthenes(input_number)
        print(prime_list)
        i = 0
        while input_number != 1:
            if input_number % prime_list[i] == 0:
                factors.add(prime_list[i])
                input_number /= prime_list[i]
            i += 1
        print(factors)
    else:
        print('Natural number must be positive and greater than 1.')
        user_input()
    return factors


def user_input():
    input_number = int(input('Please enter a natural number N: '))
    prime_factors(input_number)


def main():
    print('This program lists the prime factors of N.')
    user_input()


if __name__ == '__main__':
    main()
