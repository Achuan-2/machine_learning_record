import numpy as np

def get_beans(counts):
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = [1.2*x+np.random.rand()/10 for x in xs]
	return xs,ys

def get_beans2(counts):
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = np.array([(0.7*x+(0.5-np.random.rand())/5+0.5) for x in xs])
	return xs,ys

def get_beans3(counts):
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = np.zeros(counts)
	for i in range(counts):
		x = xs[i]
		yi = 0.7*x+(0.5-np.random.rand())/50+0.5
		if yi > 0.8:
			ys[i] = 1
	return xs,ys