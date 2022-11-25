import numpy as np

# 打印当前Numpy版本
print(np.version.version)
# 构造一个全零的矩阵，并打印其占用的内存大小
zeros = np.zeros((3, 5))
print(zeros.itemsize)
# 打印一个函数的帮助文档，比如numpy.add
print(help(np.add))
# 创建一个10-49的数组，并将其倒序排列
arange = np.arange(10, 49)
flipud = np.flipud(arange)
print(flipud)
# 找到一个数组中不为0的索引
nonzero = np.nonzero([1, 2, 3, 0])
print(nonzero)
# 随机构造一个3*3矩阵， 并打印其中最大与最小值
rand = np.random.random((3, 3))
np_max = np.max(rand)
np_min = np.min(rand)
print()
# 构造一个5*5的矩阵，令其值都为1，并在最外层加上一圈0
ones = np.ones((5, 5), dtype=np.int)
ones = np.insert(ones, 0, 0, axis=0)
ones = np.insert(ones, 6, 0, axis=0)
ones = np.insert(ones, 0, 0, axis=1)
ones = np.insert(ones, 6, 0, axis=1)
print(ones)
# 构建一个shape为(6, 7, 8)的矩阵，并找到第100个元素的索引值
random = np.random.random((6, 7, 8))
print(random)
# 对一个5*5的矩阵做归一化操作
empty = np.empty((5, 5))
empty.fill(1)
print(empty)
# 找到两个数组中相同的值
a1 = np.random.randint(0, 10, 10)
a2 = np.random.randint(0, 10, 10)
d = np.intersect1d(a1, a2)
print(d)
# 得到今天明天昨天的日期
# 得到一个月中所有的天
# 得到一个数的整数部分
# 构造一个数组，让它不能被改变
# 打印大数据的部分值，全部值
# 找到在一一个数组中， 最接近一个数的索引
np_arange = np.arange(10, 20, 1)
argmin = (np.abs(np_arange - 15.48)).argmin()
print(argmin)
# 32位float类型和32位int类型转换
# 打印数组元素位置坐标与数值
# 按照数组的某一列进 行排序
array = np.array([[1, 2, 3], [4, 16, 5], [7, 8, 9]])
sort = np.sort(array, axis=0)
print(sort)
# 统计数组中每个数值出现的次数
# 如何对一个四维数组的最后两维来求和
# 交换矩阵中的两行
# 找到一个数组中最常出现的数字
# 快速查找TOP K
# 去除掉一个数组中，所有元素都相同的数据
