

import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
import matplotlib.animation as animation

# 读入训练数据
train = np.loadtxt('data/click.csv', delimiter=',', dtype='int', skiprows=1)
train_x = train[:, 0]
train_y = train[:, 1]


# 标准化
mu = train_x.mean()
sigma = train_x.std()


def standardize(x):
    return (x - mu) / sigma


train_z = standardize(train_x)


# 预测函数一元多次项：f(x)=theta0+theta1*x+theta*x^2
# 创建X 向量： x^0，x^1，x^2 向量
def to_matrix(x):
    return np.vstack([np.ones(x.size), x, x ** 2]).T


X = to_matrix(train_z)


# 预测函数
def f(x):
    return np.dot(x, theta)

# 损失函数


def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)

#MSE 均方误差


def MSE(x, y):
    return (1 / x.shape[0]) * np.sum((y - f(x)) ** 2)


# 学习率
ETA = 1e-3

# 误差的差值
diff = 1

# 更新次数
count = 0

# 参数初始化，产生三个参数，theta0，theta1，theta2
theta = np.random.rand(3)
errors = []


# 直到误差的差值小于 0.01 为止，重复参数更新
error = MSE(X, train_y)
errors.append(error)
fig = plt.figure()
ims = []
plt.xlim(-3, 3)
plt.ylim(0, 700)
x = np.linspace(-3, 3, 100)
while diff > 1e-2:
    # 更新结果保存到临时变量
    theta = theta - ETA * np.dot(f(X) - train_y, X)

    # 计算与上一次误差的差值
    # current_error = E(X, train_y)
    errors.append(MSE(X, train_y))
    diff = errors[-2]-errors[-1]

    # 输出日志
    count += 1
    # log = '第 {} 次 : theta = {}, 差值 = {:.4f}'
    # print(log.format(count, theta, diff))
    # 动态显示f(x)变化图
    im = plt.plot(train_z, train_y, 'o', color="blue") + \
        plt.plot(x, f(to_matrix(x)))
    ims.append(im)
ani = animation.ArtistAnimation(fig, ims, interval=20, repeat_delay=1000)
ani.save("regression2_polynomial.gif", writer='pillow')

# 绘图确认
plt.clf()
plt.plot(train_z, train_y, 'o')
plt.plot(x, f(to_matrix(x)))
plt.show()


# MSE 不断在下降
x = np.arange(len(errors))
plt.plot(x, errors)
plt.show()
