import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# 获取鸢尾花数据
iris = datasets.load_iris()
# 获取特征数据和结果
X = iris.data
y = iris.target

# 获取特征数据的维度 150*4  150行4列  代表150条花的数据  4代表每个花有4个特征
print(X.shape)
# 打印前 3 行数据
print(X[:3])


def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


# 数据归一化
X = X / (X.max() + X.min()) * 0.99 + 0.01
print(X.max())
print(X.min())

# 划分测试集合训练集
X_train, X_test, y_train, y_test = train_test_split(X, y)
# 训练的数据占比75%    测试的数据占比25%
# 112*4  表示训练数据有112条记录 每条记录有4个特征
print(X_train.shape)
# 38*4 表示测试数据有38条记录 每条记录有4个特征
print(X_test.shape)
# (112,)  一维数据   数据为0,1,2  一共三种数据 表示分为三类
print(y_train.shape)
# (38,)  一维数据   数据为0,1,2  一共三种数据 表示分为三类
print(y_test.shape)
