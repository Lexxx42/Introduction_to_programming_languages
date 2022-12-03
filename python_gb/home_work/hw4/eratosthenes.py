def eratosthenes(n: int):
    sieve = set(range(2, n + 1))
    prime_list = []
    while sieve:
        prime = min(sieve)
        prime_list.append(prime)
        sieve -= set(range(prime, n + 1, prime))
    return prime_list


def main():
    n = int(input("Введите верхнюю границу диапазона: "))
    print(eratosthenes(n))


if __name__ == '__main__':
    main()
