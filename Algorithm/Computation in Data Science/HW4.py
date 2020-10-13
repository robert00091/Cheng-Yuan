import math
import random

def func_val(x):
    val = -(pow(x,5)) + 5*pow(x,3) + 20*x -5
    return val

def pso(pop, N, t):
    c_1 = c_2 = w = 1
    V_1 = []
    V_2 = [0]*N
    P = []
    i = 0
    P_g = -99999999


    for j in range(N):
        P.append(pop[j])
        if func_val(pop[j]) >= P_g:
            P_g = func_val(pop[j])
        V_1.append(0)
    i = i + 1


    while i <= t:
        r_1 = random.uniform(0,1)
        r_2 = random.uniform(0,1)

        for j in range(N):
            V_2[j] = w*V_1[j] + c_1*r_1*(P[j]-pop[j]) + c_2*r_2*(P_g-pop[j])
            pop[j] = pop[j] + V_2[j]
            if func_val(pop[j]) > func_val(P[j]):
                P[j] = pop[j]
            if func_val(pop[j]) > P_g:
                max = pop[j]
                P_g = func_val(pop[j])

        for j in range(N):
            if func_val(pop[j]) == P_g and func_val(pop[j]) == func_val(pop[j+1]):
                break
        
        i = i + 1

    print(max)
    return P_g


if __name__ == "__main__":
    pop = [-2, 0, 1, 3]
    N = 4
    t = 20
    print(pso(pop, N, t))
    
