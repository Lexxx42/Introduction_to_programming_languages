from pylab import *
fig, axes = plt.subplots(figsize=(12, 3))

x = linspace(0, 5, 10)
y = x**2

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
show()
