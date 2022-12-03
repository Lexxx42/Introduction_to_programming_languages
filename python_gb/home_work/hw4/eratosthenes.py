def eratosthenes(n: int):
    sieve = set(range(2, n + 1))
    prime_list = []
    while sieve:
        prime = min(sieve)
        prime_list.append(prime)
        sieve -= set(range(prime, n + 1, prime))
    return prime_list


def main():
    n = int(input("Please enter a natural number N: "))
    print(eratosthenes(n))


if __name__ == '__main__':
    main()
