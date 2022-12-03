# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# лист четных чисел в диапозоне от 1 до 100

# list1 = []
# for i in range(1,101):
#     #if i%2==0:
#     list1.append(i)

def f(x):
    return x ** 3


list1 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list1)
