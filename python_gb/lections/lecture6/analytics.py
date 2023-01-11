from sympy import *
from sympy.plotting import plot

x = Symbol('x')
y = Symbol('y')

f = 21 * x + 56 * y - 1034

print(solve(f, x, y))

f = x ** 2

plot(f, x)
print(f)
