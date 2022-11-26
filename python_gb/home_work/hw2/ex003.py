# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
#
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

print('This program gives a list of n numbers, '
      'filled in according to the formula (1 + 1/n) ** n and displays their sum')
print('Please enter n value for program > ', end='')
n = int(input())
n_list = []
sum_values = 0
for i in range(1, n + 1):
    value = round(((1 + 1 / i) ** i), 3)
    n_list.append(value)
print(n_list)
print(sum(n_list))
