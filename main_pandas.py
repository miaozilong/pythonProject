"""
用于数据分析和处理
"""
import pandas as pd

# 读取csv文件
df = pd.read_csv('data.csv')
# <class 'pandas.core.frame.DataFrame'>  pandas中最重要的数据类型
# 文件信息
print(df.info())
# 列名
print(df.columns)
# 读取前后N条数据  默认5条
head = df.head(10)
tail = df.tail(3)
# 设置索引
df = df.set_index(['Name'])
# 取某一列的值
age_ = df['Age']
print(age_)
# 求指标
describe = df.describe()
print(describe)
# 索引
df2 = df[['Age', 'Fare']][:5]
print(df2)
# 定位
# loc使用label进行定位 iloc用position进行定位  取第0到2行 第1列
df_slice = df2.iloc[0:3, 1:2]
loc = df2.loc['Heikkiner']
# bool类型的索引
fare_ = df['Fare'] > 40
print(fare_)
print()
# 分组
sum = df.groupby('Sex').count()

# 四则运算
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
# 求和
df_sum = df.sum()
# 使用axis=1表示按列求和
df_sum = df.sum(axis=1)
# 求均值
mean = df.mean()
# 二元统计
# 协方差
df = pd.read_csv('data.csv')
cov = df.cov()
# 相关系数
corr = df.corr()
# 相同值个数统计
counts = df['Age'].value_counts(ascending=True)
# 默认是降序  可以使用ascending=True指定升序
counts = df['Age'].value_counts(ascending=True)
# 数据段分组  bins=5表示分为5个区间段
counts = df['Age'].value_counts(ascending=True, bins=5)
print()
