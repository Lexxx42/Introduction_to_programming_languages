from pylab import *


x = linspace(0, 5, 10)
y = x**2


# figure()
# plot(x, y, 'r') # 2 массива одинаковой длины и параметр как рисовать линию r - red
# xlabel('x') # название оси
# ylabel('y') # название оси
# title('title') # как график называется
# show()

fig = plt.figure()

# left, bottom, width, height (range 0 to 1) <- main axes
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # <- inset axes
# относительные координаты относительно картинки

# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

# insert
axes2.plot(x, y, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title')
show()
