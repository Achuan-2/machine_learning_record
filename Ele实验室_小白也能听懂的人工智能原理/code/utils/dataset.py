import numpy as np

def get_beans(counts):
	"""
	一个神经元，激活函数为y=wx+
	"""
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = [1.2*x+np.random.rand()/10 for x in xs]
	return xs,ys

def get_beans2(counts):
	"""
	一个神经元，激活函数为y=wx+b
	"""
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = np.array([(0.7*x+(0.5-np.random.rand())/5+0.5) for x in xs])
	return xs,ys

def get_beans3(counts):
	"""
	一个神经元，激活函数为sigmoid
	"""
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = np.zeros(counts)
	for i in range(counts):
		x = xs[i]
		yi = 0.7*x+(0.5-np.random.rand())/50+0.5
		if yi > 0.8:
			ys[i] = 1
	return xs,ys


def get_beans4(counts):
	"""
	一层隐藏层，激活函数为sigmoid
	"""
	xs = np.random.rand(counts)*2
	xs = np.sort(xs)
	ys = np.zeros(counts)
	for i in range(counts):
		x = xs[i]
		yi = 0.7*x+(0.5-np.random.rand())/50+0.5
		if yi > 0.8 and yi < 1.4:
			ys[i] = 1

	return xs, ys


def get_beans5(counts):
	xs = np.random.rand(counts, 2)*2
	ys = np.zeros(counts)
	for i in range(counts):
		x = xs[i]
		if (x[0]-0.5*x[1]-0.1) > 0:
			ys[i] = 1
	return xs, ys


def get_beans6(counts):
	xs = np.random.rand(counts, 2)*2
	ys = np.zeros(counts)
	for i in range(counts):
		x = xs[i]
		if (np.power(x[0]-1, 2)+np.power(x[1]-0.3, 2)) < 0.5:
			ys[i] = 1

	return xs, ys
