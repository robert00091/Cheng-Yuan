import math
import random
import numpy as np


def func_val(x):
    val = pow(x, 5) - 5*pow(x, 3) - 20*x + 5
    return val


def aco(pop, N, n, t):
    # a: pheromone
    a = [[1 for x in range(n)] for y in range(N)]
    l = 1
    f_best = 999999
    f_worst = -999999
    x_best = 0
    x_worst = 0

    prob = 0.5
    c = 2

    while l <= t:
        P = [[0 for x in range(n)] for y in range(N)]
        for i in range(N):
            total = sum(a[i])
            for j in range(n):
                p = pow(a[i][j], l)/total
                P[i][j] = P[i][j] + p*j
        # print(P)
        for i in range(N):
            x = [0]*N
            r = [0]*N
            r[i] = random.uniform(0, 1)
            for j in range(1, n):
                if P[i][j-1] <= r[i] <= P[i][j]:
                    x[i] = pop[j-1]

                if func_val(x[i]) <= f_best:
                    x_best = x[i]
                    f_best = func_val(x_best)
                    #print(x_best, func_val(x_best))

                if func_val(x[i]) >= f_worst:
                    x_worst = x[i]
                    f_worst = func_val(x_worst)

                # Update the pheromone a
                a[i][j] = (1-prob)*a[i][j]
                if j == x_best:
                    a_1 = c * func_val(x_best)/func_val(x_worst)
                    a[i][j] = a[i][j] + a_1

        l = l+1
    return x_best


if __name__ == "__main__":
    pop = np.arange(0, 3.5, 0.5)
    N = 4
    n = 7
    t = 2
    x_best = aco(pop, N, n, t)
    print('Minimum is at', x_best, 'with value', func_val(x_best))
