# -*- coding: utf-8 -*-

# -- Sheet --

from random import uniform
from sympy.solvers import solveset
from sympy.plotting import plot
from sympy import Symbol, Reals, Interval, diff, oo, is_increasing

"""Variable declaration."""

x = Symbol('x')

"""First function."""
f = -18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

"""Second function."""
# f = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18

"""Third function."""
# f = (x ** 2 + 3) / (3 * (x + 1))

"""Equation roots."""

print(solveset(f, x, Reals).evalf(3))

"""Intervals of enc/dec function."""

dif_list = [-oo, oo]
dif_list[1:1] = solveset(diff(f), x, Reals).evalf(3)
decrease, increase = [], []
for i in range(1, len(dif_list)):
    a = is_increasing(f, Interval.open(dif_list[i - 1], dif_list[i]))
    if a:
        increase.append((dif_list[i - 1], dif_list[i]))
    else:
        decrease.append((dif_list[i - 1], dif_list[i]))
print("Increasing: ", ", ".join(str(i) for i in increase))
print("Decreasing: ", end='')
print(*decrease, sep=', ')

"""Graph plotting."""

"""First function."""
plot(f, (x, -0.6, 0.6))

"""Second function."""
# plot(f, (x, -4, 4))

"""Third function."""
# plot(f, (x, -1.025, -0.975))

"""Calculation of vertex."""

dataset = sorted(solveset(diff(f), x, Reals).evalf(3))
dataset.insert(0, dataset[0] - 1)

dif = diff(f)

data_list = []

for i, item in enumerate(dataset):
    data_list.append(dif.subs(x, uniform(item, dataset[i] + 1)))
    if i:
        if data_list[i - 1] < 0 < data_list[i]:
            print(f"min:  {(item, f.subs(x, item).evalf(3))}")
        elif data_list[i - 1] > 0 > data_list[i]:
            print("max: ", (item, f.subs(x, item).evalf(3)))

"""Determination of intervals where f > 0."""

print(f"f>0: {solveset(f > 0, x, Reals).evalf(3)}")
solveset(f > 0, x, Reals).evalf(3)

"""Determination of intervals where f < 0."""

print("f<0:", solveset(f < 0, x, Reals).evalf(3))
solveset(f < 0, x, Reals).evalf(3)
