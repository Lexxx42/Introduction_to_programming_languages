# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

from math import sqrt


def discr(a:int, b:int, c: int):
    res = b**2-4*a*c
    with open ('new_file.txt','a',encoding='utf-8') as F:
        if res>0:
            sqr1 = (-b+sqrt(res))/(2*a)
            sqr2 = (-b-sqrt(res))/(2*a)
            F.writelines([f'{sqr1}, {sqr2}\n'])
        elif res ==0:
            sqr1 = -b/(2*a)
            F.write(f'{sqr1}\n')
        else:
            F.write('нет корней\n')

for i in range(3):
    a,b,c = int(input()), int(input()), int(input())
    discr(a,b,c)

