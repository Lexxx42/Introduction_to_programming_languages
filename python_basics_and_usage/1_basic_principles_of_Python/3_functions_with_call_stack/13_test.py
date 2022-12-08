# # Дана функция s﻿:

# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
# В результате каких вызовов данная функция вернет число 31?

# s(11, 10)  # 31

# def s(a, *vs, b=10):  a=11, b=10
#    res = a + b  11+10=21
#    for v in vs: 10
#        res += v 31
#    return res  31

def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


print(s(11, 10))

# s(11, 10, 10)  # 41


def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res


print(s(11, 10, 10))

# s(5, 5, 5, 5, 1)  # 31

def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res

print(s(5, 5, 5, 5, 1))

# s(0, 0, 31)  # 41

def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res

print(s(0, 0, 31))

# s(b=31, 0)  # errro!

# def s(a, *vs, b=10):
#     res = a + b 
#     for v in vs:
#         res += v
#     return res

# print(s(b=31, 0))

# s(21)  # 31
def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res

print(s(21))

# s(11, 10, b=10)  # 31

def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res

print(s(11, 10, b=10))

# s(11, b=20)  # 31

def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res

print(s(11, b=20))

# s(b=31)  # error!

def s(a, *vs, b=10):
    res = a + b 
    for v in vs:
        res += v
    return res

print(s(b=31))
