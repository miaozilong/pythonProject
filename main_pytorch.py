import torch

# 创建Tensor
# 直接传入具体的值
a = torch.Tensor(([2, 2], [3, 4]))
# 按照形状定义   定义2*3的张量   默认数据是内存中未初始化的值
a = torch.Tensor(2, 3)
# 定义全为1的张量
a = torch.ones(2, 3)
# 定义单位张量
a = torch.eye(4, 3)
# 定义全0的张量
a = torch.zeros(5, 5)
# 随机
a = torch.rand(2, 4)
# 正态分布
a = torch.normal(mean=0, std=torch.rand(5))
# 数列
a = torch.arange(10, 20, 1)
a = torch.linspace(10, 20, 7)
# print(a)
# print(a.storage_type())
# print(type(a))

# 获取设备
cpu = torch.device('cpu')
a = torch.tensor([2, 2], device=cpu, dtype=torch.float64)
# 稀疏张量 默认是稠密的张量
# 坐标
coordinate = torch.tensor([[0, 1, 2], [0, 1, 2]])
# 值
value = torch.tensor([1, 2, 3])
# 形状
shape = (4, 4)
a = torch.sparse_coo_tensor(coordinate, value, shape)

# tensor的算术运算
# 加减乘除 矩阵运算 幂运算 对数运算
"""
加法
c = a+b
c = torch.add(a,b)
c = a.add(b)
a.add_(b)
前三种结果都一致，第四种下划线表示会修改a的值

减乘除和加法类似

点乘
c = a @ b
c = torch.mm(a, b)
c = a.mm(b)
c = torch.matmul(a, b)  
一般使用第一种方式，写法更简单

在高维度张量运算时，本质时对最后两维进行点乘，所以要求前面的维度都保持一致
"""
a = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# c = a + b
# c = torch.add(a, b)
# c = a.add(b)
# a.add_(b)
# c = a @ b
# c = torch.mm(a, b)
# c = a.mm(b)
a = torch.ones(1, 2, 3, 4)
b = torch.ones(1, 2, 4, 3)
c = a @ b
"""
幂运算
c = a ** 2
c = torch.pow(a, 2)

e的底的幂运算
c = torch.exp(a)
"""
c = a ** 2
c = torch.pow(a, 2)
c = torch.exp(a)
print(c)

