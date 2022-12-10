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

n = int(input())
list_input = [i for i in range(20, n + 1)]
print(list(filter(lambda x: not x % 20 or not x % 21, list_input)))
