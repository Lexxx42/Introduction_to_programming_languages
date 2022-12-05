# Актуальные ссылки из лекции:

# https://matplotlib.org/2.0.2/gallery.html

# https://github.com/jrjohansson/scientific-python-lectures

# https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb

# https://www.geeksforgeeks.org/matplotlib-pyplot-xkcd-in-python/

from pylab import *


x = linspace(0, 5, 10)
y = x**2
print(x)
# [0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
#  3.33333333 3.88888889 4.44444444 5.        ]
print(y)
# [ 0.          0.30864198  1.2345679   2.77777778  4.9382716   7.71604938
#  11.11111111 15.12345679 19.75308642 25.        ]

figure()
plot(x, y, 'r')  # 2 массива одинаковой длины и параметр как рисовать линию r - red
xlabel('x')  # название оси
ylabel('y')  # название оси
title('title')  # как график называется
show()
