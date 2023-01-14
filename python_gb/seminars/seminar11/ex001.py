from sympy import *
from sympy.plotting import plot

"""https://datalore.jetbrains.com/notebook/7XLGHiMrD4HKQPt8ekVv6S/Mtk6ncHEy8WLBlO2H3DpN2/"""

x = Symbol('x')
f = 5 * x ** 2 + 10 * x - 30

solveset(f, x, Reals).evalf(3)

dif_list = [-oo, oo]
dif_list[1:1] = solveset(diff(f), x, Reals).evalf(3)
decrease, increase = [], []
for i in range(1, len(dif_list)):
    a = is_increasing(f, Interval.open(dif_list[i-1], dif_list[i]))
    if a:
        increase.append((dif_list[i-1], dif_list[i]))
    else:
        decrease.append((dif_list[i-1], dif_list[i]))
print("Increasing: ", *increase)
print("Decrease: ", *decrease)

plot(f, (x, -1.5,-0.5))

from random import uniform

dataset = sorted(solveset(diff(f), x, Reals).evalf(3))
dataset.insert(0, dataset[0]-1)

dif = diff(f)

my_lst = []

for i, item in enumerate(dataset):
    my_lst.append(dif.subs(x, uniform(item, dataset[i]+1)))
    if i != 0:
        if my_lst[i-1] < 0 < my_lst[i]:
            print("min: ", item, f.subs(x, item).evalf(3))
        elif my_lst[i-1] > 0 > my_lst[i]:
            print("max: ", item, f.subs(x, item).evalf(3))

print("f>0:",solveset(f>0, x, Reals).evalf(3))
solveset(f>0, x, Reals).evalf(3)


print("f<0:",solveset(f<0, x, Reals).evalf(3))
solveset(f<0, x, Reals).evalf(3)
