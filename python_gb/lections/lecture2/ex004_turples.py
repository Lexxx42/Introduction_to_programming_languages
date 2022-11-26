# Кортежи
# кортеж - это неизменяеммый "список"
import turtle

t = ()
print(type(t))  # <class 'tuple'>

t = (1,)
print(type(t))  # <class 'tuple'>

t = (1)
print(type(t))  # <class 'int'>

colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
t = tuple(colors)
print(t)  # ('red', 'green', 'blue')

a, b = 3, 4
print(a, b)  # 3 4
a = (3, 1, 7, 4)
# a = (3,)  # кортеж из 1-го элемента
print(a)  # (3, 4)
print(a[0])  # 3
print(a[-1])  # 4

print()
# a[0] = 12  # TypeError: 'tuple' object does not support item assignment
a = (3, 1, 7, 4)
for item in a:
    print(item)

colors = ['red', 'green', 'blue']
t = tuple(colors)
red, green, blue = t
print('r: {} g: {} b: {}'.format(red, green, blue))  # r: red g: green b: blue
