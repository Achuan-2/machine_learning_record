

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import gif
import matplotlib.animation as animation
train = np.loadtxt('data/click.csv', delimiter=',', dtype='int', skiprows=1)
train_x = train[:, 0]
train_y = train[:, 1]



mu = train_x.mean()
sigma = train_x.std()

# zscore 标准化，mean变为0，sigama变为1
def standardize(x):
    return (x - mu) / sigma


train_z = standardize(train_x)


# 预测函数 一元一次：f(x)-theta0+theta1*x
def f(x):
    return theta0 + theta1 * x
# 目标函数
def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


#代价函数
theta1 = np.arange(-10, 10, 0.1)
theta0 = np.arange(-10, 10, 0.1)
theta1, theta0 = np.meshgrid(theta1, theta0)
print(theta1)  # 打印出来瞅瞅
print(theta0)


es = 0
#因为theta1和theta0已经变成了网格矩阵了
#一次性带入全部计算，我们需要一个一个的算
n = len(train_y)
for i in range(n):
	y_pre = theta1*train_x[i]+theta0  # 取出一个样本在网格矩阵上计算，得到一个预测矩阵
	e = (train_y[i]-y_pre)**2  # 标准值减去预测（矩阵）得到方差矩阵
	es += e  # 把单样本上的方差矩阵不断累加到es上
es = es/n  # 求平均值，这样es方差矩阵每个点的位置就是对应的theta1和theta0矩阵每个点位置预测得到的方差
fig = plt.figure()
ax = Axes3D(fig)
ax.set_zlim(0, 500000)

#plot_surface函数绘制曲面
#cmap='rainbow表示彩虹图（用不同的颜色表示不同值）
ax.plot_surface(theta1, theta0, es, cmap='rainbow')
#显示图像
plt.show()

# 学习率
ETA = 1e-3
# 误差的差值
diff = 1
# 更新次数
epoch = 0
# 参数初始化
theta0 = np.random.rand()
theta1 = np.random.rand()
# 直到误差的差值小于 0.01 为止，重复参数更新
error = E(train_z, train_y)
errors = []
errors.append(error)

# ？这里用diff来判断是否停止循环，也就是当收敛时停止循环，我看有些人的代码是用epoch来规定迭代次数，所以机器学习里是用哪一个？
fig = plt.figure()
ims = []
plt.xlim(-3, 3)
plt.ylim(0, 700)
x = np.linspace(-3, 3, 100)
while diff > 1e-2:
    # 更新结果保存到临时变量 (问：为什么要先保存在临时变量中？ 答：为了同时更新参数，不然一个直接改了，另一个参数的更新也在改变)
    tmp_theta0 = theta0 - ETA * np.sum((f(train_z) - train_y))
    tmp_theta1 = theta1 - ETA * np.sum((f(train_z) - train_y) * train_z)

    # 更新参数
    theta0 = tmp_theta0
    theta1 = tmp_theta1

    # 计算与上一次误差的差值
    error = E(train_z, train_y)
    errors.append(error)
    diff = abs(errors[-2]-errors[-1])
    # 输出日志
    epoch += 1
    log = 'Epoch {}  : theta0 = {:.3f}, theta1 = {:.3f}, diff = {:.4f}'
    print(log.format(epoch, theta0, theta1, diff))

    # 动态显示f(x)变化图
    # plt.text(0.8, 1, f'Epoch:{epoch:},Loss:{error:.2f}')
    im = plt.plot(train_z, train_y, 'o', color="blue") + plt.plot(x, f(x))
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=20, repeat_delay=1000)
ani.save("regression1_linear.gif", writer='pillow')

# # 绘图确认
plt.clf()
plt.plot(train_z, train_y, 'o')
plt.plot(x, f(x))
plt.show()



# # error 不断在下降
x = np.arange(len(errors))
plt.plot(x, errors)
plt.show()



