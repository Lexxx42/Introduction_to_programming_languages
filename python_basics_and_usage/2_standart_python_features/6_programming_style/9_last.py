# Кроме стиля программирования читаемость вашего кода могут повысить документирующие строки.
# Вы можете использовать строку в начале тела вашей функции, метода или класса
# и написать в ней что делает ваша функция, метод или класс.

# При этом данная строку будет доступна в качестве атрибута __doc__.

from random import random


class RandomIterator:
    """
    RandomIterator(k) - new iterator for k random numbers in (0, 1)

    Uses random.random
    """

    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


print(RandomIterator.__doc__)

# Большая часть стандартной библиотеки python также использует этот механизм документации.
# Поэтому мы можем смотреть документацию для стандартных функций, классов и даже модулей.

import sys

print(sys.__doc__)
print('*********')
print(sys.getrefcount.__doc__)
