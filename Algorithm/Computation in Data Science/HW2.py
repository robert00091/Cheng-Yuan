import numpy
import random

global x_1, x_2

def f(X):
    return 6*pow(X[0], 2) - 6*X[0]*X[1] + 2*pow(X[1], 2) - X[0] -2*X[1]

def random_sampling(x_1, x_2):
    xb = [x_1, x_2]
    pb = [0]*2

    count = 0

    while count != 100000:
        pb[0] = random.uniform(-100, 100)
        pb[1] = random.uniform(-100, 100)

        if f(pb) < f(xb):
            xb[0], xb[1] = pb[0], pb[1]

        count = count + 1

    print(xb)
    print('min:', f(xb))




# Random Walk
def rand_walk(x_1, x_2):
    xb = [random.uniform(-100, 100) for i in range(2)]
    pb = [0]*2
    x_best = [xb[0], xb[1]]

    count = 0
    while count < 10000:
        
        for dist in range(-10, 11):
            move_1 = [xb[0] + dist]
            move_2 = [xb[1] + dist]
        
        for i in move_1:
            for j in move_2:
                pb = [i, j]
                if f(pb) < f(x_best):
                    x_best[0], x_best[1] = pb[0], pb[1]

        xb = [random.uniform(-100, 100) for i in range(2)]

        count = count + 1

    print(x_best)
    print('min:', f(x_best))
             




if __name__ == "__main__":
    x_1, x_2 = 20, 0
    random_sampling(x_1, x_2)

    rand_walk(x_1, x_2)
