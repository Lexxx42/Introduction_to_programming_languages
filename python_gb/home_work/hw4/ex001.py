# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from decimal import Decimal, ROUND_HALF_UP


def round_decimal(number: Decimal, rounding: Decimal) -> Decimal:
    output = Decimal(number.quantize(Decimal(str(rounding)[1:]), rounding=ROUND_HALF_UP))
    print(output)
    return output


def user_input() -> tuple[Decimal, Decimal]:
    real_number = Decimal(input('Enter a real number: '))
    accuracy = Decimal(input("Enter the required accuracy '0.0001': "))
    if 1 <= accuracy or accuracy.is_signed():
        print('Accuracy must be positive and lower than 1.')
        user_input()
    return real_number, accuracy


def main() -> None:
    print('This program calculates a number with a given precision.')
    real_number, accuracy = user_input()
    round_decimal(real_number, accuracy)


if __name__ == '__main__':
    main()
