print("Программа получает на вход 5 чисел и сравнивает их между собой. Выдает максимум и минимум")

num_max = 0
for i in range(5):
    a = int(input())
    if a > num_max:
        num_max = a

print("max=", num_max)
