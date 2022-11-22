
# Общий вид конструкции условия
# if условие_1:
# блок_1
# elif условие_2:
# блок_2
# else:
# блок_3

# когда одно условие выполнилось дальнейшие условия выполняться не будут

# найти наибольшее из двух чисел

from re import A


a = 4
b = 7

# without additional var
if a >= b:
    print(a)
else:
    print(b)


# with additional var
m = a
if b > m:
    m = b
print(m)
