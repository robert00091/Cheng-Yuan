import random
import numpy as np

'''
Search space: (i, j, k, l) ---> max value position
Input:
Objective function: X(i, j, k, l) ---> max value
y: the lowest possible objectve value, y=0.9999 (upper bound)
'''
y = 1 # upper bound

## Exhaustive Enumeration
def ex_eumeration(n, X):
	i, j, k, l = 0, 0 ,0, 0
	xb = X[i][j][k][l]

	count = 0 
	
	while count != pow(n, 4) and xb < y:
		for i in range(n):
			for j in range(n):
				for k in range(n):
					for l in range(n):
						if X[i][j][k][l] > xb: 
							xb = X[i][j][k][l]
							i_new, j_new, k_new, l_new = i, j, k, l
						count = count + 1	

	print('i, j, k, l:', i_new, ',', j_new, ',', k_new, ',', l_new)	
	#print(X[i_new][j_new][k_new][l_new])
	print('max:', xb)

	return xb


## gb: the global best vlaue = xb
## Termination criterion: pb >= 0.95gb or #of iteration = 100 

## Randon Sampling
def rand_sampling(n, X, gb):
	i, j, k, l = [random.randint(0, n-1) for i in range(4)]
	pb = X[i][j][k][l]

	count = 0
	while pb < 0.95*gb or count < 100:
		i_new, j_new, k_new, l_new = [random.randint(0, n-1) for i in range(4)]
		if (i_new, j_new, k_new, l_new) != (i, j, k, l):
			pb_new = X[i_new][j_new][k_new][l_new] 
			if pb_new > pb:
				pb = pb_new
				i, j, k, l = i_new, j_new, k_new, l_new
			count = count + 1
			#print(count)
	print('i, j, k, l:', i, ',', j, ',', k, ',', l)	
	#print(X[i][j][k][l])
	print('max:', pb)


## The mutation of a candidate solution as it randomly chooses a new position within
## 1 step of each axis. 

## Hill Climbing
def hill_climbing(n, X, gb):
	i, j, k, l = [random.randint(0, n-1) for i in range(4)]
	pb = X[i][j][k][l]

	count = 0
	while pb < 0.95*gb or count < 100:
		i_new, j_new, k_new, l_new = [i+1, i-1], [j+1, j-1], [k+1, k-1], [l+1, l-1]

		for i in i_new:
			for j in j_new:
				for k in k_new:
					for l in l_new:
						print(i,j,k,l)
						pb_new = X[i][j][k][l] 
						if pb_new > pb:
							pb = pb_new
							#i, j, k, l = i_new, j_new, k_new, l_new
						count = count + 1	

	print('i, j, k, l:', i, ',', j, ',', k, ',', l)	
	#print(X[i][j][k][l])
	print('max:', pb)


if __name__ == "__main__":
	n = 4
	x = np.zeros(pow(n,4))
	for i in range(pow(n,4)):
		val = random.uniform(0,1)
		x[i] = val

	print(x)

	X = np.reshape(x, (n, n, n, n))

	print('Method 1: Exhaustive enumeration')
	gb = ex_eumeration(n, X)


	print('\nMethod 2: Random sampling')
	rand_sampling(n, X, gb)

	print('\nMethod 3: Hill climbling')
	hill_climbing(n, X, gb)

	#print(X.shape)




