import numpy
import random
import math

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

    return xb




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
    
    return x_best

# Simulated Annealing
def simul_anneling(X):
    pcur = f(X)
    #print(X)
    pbest = pcur
    T = 100000
    c = 0.2
    pb = [0]*2
    move_1, move_2 = [], []


    count = 0
    while count < 50 and T > 0:
        for dist in numpy.arange(-1,1,0.5):
            x_1 = X[0] + dist
            x_2 = X[1] + dist
            move_1.append(x_1)
            move_2.append(x_2)
            #print(move)

        for i in move_1:
            for j in move_2:
                pb[0], pb[1] = i, j
                #print(pb)
                pnew = f(pb)

                dE = pnew - pcur
                if dE <= 0:
                    X[0], X[1] = pb[0], pb[1]
                    pcur = pnew
                    if pcur < pbest:
                        pbest = pcur
                # dE > 0: using the Metropolis criterion
                else:        
                    rv = random.uniform(0,1)
                    if rv < math.exp(-dE/T):
                        pcur = pnew
                        T = T * c
                    
        count = count + 1

    print(X)
    print(pbest)

if __name__ == "__main__":
    x_1, x_2 = 20, 0
    X_1 = random_sampling(x_1, x_2)

    print('Random walk:')
    X = rand_walk(x_1, x_2)

    print('Simulated annealing:')
    simul_anneling(X_1)
