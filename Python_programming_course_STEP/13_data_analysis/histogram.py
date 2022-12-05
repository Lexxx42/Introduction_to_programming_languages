# Построение гистограмм
from numpy import *
from pylab import *


n = np.random.randn(10000)

fig, axes = plt.subplots(1,2, figsize=(12,4))  # 12, 4 - размер в дюймах

axes[0].hist(n)
axes[0].set_title('default histogram')
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)  # bins - количество вертикальных столбцов в графике
axes[1].set_title('cumulative detailed histogram')
axes[1].set_xlim((min(n), max(n)))

show()

