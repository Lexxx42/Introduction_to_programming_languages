# Локальные переменные

# def init_values():
#     a=100
#     b=200
#
# init_values()
# print(a+b)  # error! no a and b


# def init_values():
#     a = 100
#
#
# a = 0
# init_values()
# print(a)  # a=0


def init_values(a):
    a = 100


b = 0
init_values(b)
print(b)  # b=0


# Изменение объектов, связанных с локальными переменными

def append_zero(xs):
    xs.append(0)


a = []
append_zero(a)
print(a)
