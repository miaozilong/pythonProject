import numpy as np

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 转成nparray类型
a = np.array(l)
# <class 'numpy.ndarray'>
print(type(a))
print(a)
# int32  nparray中要求是相同的数据类型，如果不同，会内部转为相同的类型，如整形和浮点型混用，则元素都会都转成浮点类型,也可使用dtype参数指定数据类型 如dtype = np.str  当指定为np.object时,可以存入混合类型 不会自动转换
print(a.dtype)
# (3,3) 数组的形状
print(a.shape)
# 9  元素的个数
print(a.size)
# 2 维度
print(a.ndim)
# 把所有元素填充为0
# a.fill(0)
# 使用索引取值  a[2][2]和a[2,2]都可以
print(a[2, 2])
# 取其中一个维度 a[2]在这里表示第三行
print(a[2])
# 按列取值  :表示所有行都取,也可使用0:2来取第0行和第1行  1表示取第2列
print(a[:, 1])
# 数组的切片
a1 = a[1:3]
print(a1)
# 复制变量
a2 = a
# True 内存中只有一份值
print(id(a2) == id(a))
# 复制数组
a3 = a.copy()
# False 使用copy后，内存中复制一份值
print(id(a3) == id(a))
# 复制并转换数据类型 使用asarray函数  也可使用a.astype(dtype=np.float64)来复制转换
a4 = np.asarray(a, dtype=np.float64)
# False 不再是同一个对象
print(id(a4) == id(a))
# 构建等差数列
a5 = np.arange(0, 100, 10)
print(a5)
## 随机数
# 产生10个随机数
rand = np.random.rand(10)
print(rand)
# 数组的运算
a1 = a.copy()
a2 = a.copy()
# 求和
## 对所有数求和
a__sum = np.sum(a1)
## 按轴求和  这里0表示按照竖直方向,1表示水平方向
np_sum_ax0 = np.sum(a1, axis=0)
np_sum_ax1 = np.sum(a1, axis=1)
# 求积 同样可以使用axis按轴求
prod = np.prod(a1)
# 求最值和最值索引位置 同样可以使用axis按轴求
np_min = np.min(a)
np_max = np.max(a)
argmin = np.argmin(a)
argmax = np.argmax(a)
# 求均值
mean = a.mean()
# 求标准差
std = a.std()
# 求方差
var = a.var()
# 极值收拢  小于2的值都会变成2,大于7的值都会变成7
clip = a.clip(2, 7)
# 四舍五入  可以使用decimal参数指定精度
a_round = a.round()
# 排序
sort = np.sort(a)
# 矩阵上下翻转
flipud = np.flipud(a)

# 数组形状
a1 = np.arange(10)
# 修改为2*5的矩阵  大小不能改变 否则会报错
a1.shape = (2, 5)
# 修改为5*2的矩阵
a1.reshape(5, 2)
# 矩阵的转置  使用transpose方法和T属性都可以
transpose = a1.transpose()
t = a1.T
# 数组的连接
# 默认水平拼接  可使用axis=1 表示纵向拼接
concatenate = np.concatenate((a1, a1), axis=1)
# 水平拼接
hstack = np.hstack((a1, a1))
# 纵向拼接
vstack = np.vstack((a1, a1))

# 矩阵的生成函数
# 等差数列
arange = np.arange(10, 20, 2)
# 在10到100之间按照等差方式等间距构造300个数字,包括10和100
linspace = np.linspace(10, 100, 300)
# 构造3*5的0矩阵
zeros = np.zeros((3, 5))
# 构造3*5的1矩阵
ones = np.ones((3, 5), dtype=np.int)
# 根据形状构造0矩阵   同样有ones_like函数用于根据形状构造1矩阵
like = np.zeros_like(ones)
# 构造5*5的单位矩阵
identity = np.identity(5)
# 填充数据   修改自身的值,返回None
fill = ones.fill(8)

# 矩阵的运算
a1 = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
a2 = a1.copy()
# 数乘
a_ = a1 * a2
multiply = np.multiply(a1, a2)
# 点乘
dot = a1.dot(a2)
# 随机
# 构建3*2的随机矩阵 所有值都是从0到1
random_rand = np.random.rand(3, 2)
# 构建3*2的10到20之间的整数矩阵 包括10 不包括20
randint = np.random.randint(10, 20, (3, 2))
# 高斯分布
mu, sigma = 0, 0.1
normal = np.random.normal(mu, sigma, 20)
# 洗牌
np_arange = np.arange(1, 10)
np.random.shuffle(np_arange)
# 文件读写  也可以使用savetxt和loadtxt方法进行文本存取
np.save('data.npy', a)
load = np.load('data.npy')
print()
