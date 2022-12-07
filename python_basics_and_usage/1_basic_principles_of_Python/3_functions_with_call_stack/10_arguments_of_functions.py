# Примеры вызова функций
def printab(a, b):
    print(a)
    print(b)


# Correct way to call function
printab(10, 20)  # позиционные аргументы, так как порядок их написания важен
printab(b=20, a=10)  # именованные аргументы
# keyword arguments always after non-keyword arguments
printab(10, b=20)

lst = [10, 20]
printab(*lst)  # == printab(lst[0], lst[1])

args = {'a': 10, 'b': 20}
printab(**args) # == printab(key1 = args[key1], key2 = args[key2])
# * - keys into printab()
# ** - values into printab()
