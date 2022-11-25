import matplotlib
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pylab import mpl
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.sans-serif'] = ['simsun']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 折线图    -- 表示虚线  :表示点线   color标识颜色
# s = np.array([1, 2, 3, 4, 5, 6])
# plt.plot(s, s, '-', color='#f00')
# plt.plot(s, s ** 2, color='#000')
# x = np.linspace(-10, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# 设置轴的标签
# plt.xlabel('体积')
# plt.ylabel('重量')
# plt.title('标题')
# plt.text(0, 0, '原点')
# 绘制格子
# plt.grid()
# 子图
# 211表示2行1列,最后一个1表示子图中的序号
# plt.subplot(211)
# plt.plot(x, y)
# plt.subplot(212)
# plt.plot(2 * x, y)

# 柱状图
# count = 1500
# x = np.arange(count)
# y = np.random.randn(count)
# plt.bar(x, y)

# 三维图  有问题  图没出来
figure = plt.figure()
ax = Axes3D(figure)
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(x, y)
Z = np.sin(X + Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
