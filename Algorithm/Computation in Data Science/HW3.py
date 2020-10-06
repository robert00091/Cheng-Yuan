import numpy as np
import itertools
import random


def pop_input(knife, pistol, equipment, primary):

    tmp, tmp_1, tmp_2, tmp_3 = [], [], [], []

    bound = 529
    sum_1 = []
    count = 0

    pop = []

    a = [3.3, 3.4, 6.0, 26.1, 37.6, 62.5, 24.2, 32.1, 42.5]
    arr = [3.3, 3.4, 6.0, 26.1, 37.6, 62.5, 100.2, 141.1,
           119.2, 122.4, 247.6, 352.0, 24.2, 32.1, 42.5]

    for i in range(len(a)+1):
        tmp.append(list(itertools.combinations(a, i)))

    tmp = [y for x in tmp for y in x if len(y) != 0]
    # print(tmp)
    # print(len(tmp))

    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i][j] in knife:
                tmp_1.append(tmp[i])
                break
    # print(tmp_1)
    for i in range(len(tmp_1)):
        for j in range(len(tmp_1[i])):
            if tmp_1[i][j] in pistol:
                tmp_2.append(tmp_1[i])
                break
    # print(tmp_2)
    for i in range(len(tmp_2)):
        for j in range(len(tmp_2[i])):
            if tmp_2[i][j] in equipment:
                tmp_3.append(tmp_2[i])
                break

    pop = tmp_3
    pop_x = []

    for i in range(len(pop)):
        X = [0]*15
        for j in range(len(pop[i])):
            if pop[i][j] in arr:
                k = arr.index(pop[i][j])
        # print(k)
                X[k] = 1
        pop_x.append(X)

    for i in range(len(tmp_3)):
        sum_1.append(sum(tmp_3[i]))

    prima = []
    for i in range(len(primary)+1):
        prima.append(list(itertools.combinations(primary, i)))

    prima = [y for x in prima for y in x if len(y) != 0]

    sum_3 = []
    prima_3 = []
    for i in range(len(prima)):
        for j in range(len(prima[i])):
            if sum(prima[i]) <= 529:
                sum_3.append(sum(prima[i]))
                prima_3.append(prima[i])

    count = 0
    prim3_idx = []
    pop_idx = []
    sumup = 0
    k = []

    for i in range(len(tmp_3)):
        for j in range(len(prima)):
            sum_k = sum(tmp_3[i])
            sum_p = sum(prima[j])
            if sum_k + sum_p <= 529:
                p = tmp_3[i]+prima[j]
                k.append(p)

        count = count + 1
    pop_prima = []
    for i in range(len(k)):
        X_k = [0]*15
        for j in range(len(k[i])):
            if k[i][j] in arr:
                k_pop = arr.index(k[i][j])
                X_k[k_pop] = 1
        pop_prima.append(X_k)
    pop_input = pop_x + pop_prima

    return pop_input


def two_combinations(matepool):

    return list(itertools.combinations(matepool, 2))

def flatten(A):
    return [y for x in A for y in x]

def roul_wheel(pop, ps, mps):
    A = []
    matepool = []
    sur_pts = [7, 8, 13, 29, 48, 99, 177, 213, 202, 210, 380, 485, 9, 12, 15]
    sur_sum = 0
    max = -99999999
    for i in range(ps):
        for j in range(15):
            sur_sum = sur_sum + pop[i][j]*sur_pts[j]
        a = sur_sum
        A.append(a)
        if a > max:
            max = a
        sur_sum = 0

    sum = 0
    for i in range(ps):
        sum = sum + (max-A[i])
        A[i] = sum

    for i in range(mps-1):
        a = random.randint(0, sum)
        max_i = 0
        if A[i] <= a:
            max_i = i
        matepool.append(pop[max_i])
    return matepool


def two_pt_cross(gp1, gp2):

    gp1_tmp = []
    gp2_tmp = []
    mate_two_cross = []

    gp1_tmp_1 = gp1[0:5]
    gp1_tmp_2 = gp1[10:15]
    gp2_tmp_1 = gp2[0:5]
    gp2_tmp_2 = gp2[10:15]

    gp1[0:5] = gp2_tmp_1
    gp1[10:15] = gp2_tmp_2
    mate_two_cross.append(gp1)

    gp2[0:5] = gp1_tmp_1
    gp2[10:15] = gp1_tmp_2
    mate_two_cross.append(gp2)

    return mate_two_cross


def multi_bit_mut_rand(gp, eta):
    g = gp
    #print(g)
    while eta != 0:
        for i in range(len(gp)):
            
            j = random.randint(0, 14)
            k = random.randint(0, 14)
            if k == j: 
                k = random.randint(0, 14)
            #print('--------------%d, %d------------------'%(j, k))
            #print(g[i])
            if g[i][j] == 0:
                g[i][j] = 1
            else:
                g[i][j] = 0

            if g[i][k] == 0:
                g[i][k] = 1
            else:
                g[i][k] = 0

            #print(g[i])
            
        eta = eta - 1
    return g



if __name__ == "__main__":

    knife = [3.3, 3.4, 6.0]
    pistol = [26.1, 37.6, 62.5]
    equipment = [24.2, 32.1, 42.5]
    primary = [100.2, 141.1, 119.2, 122.4, 247.6, 352.0]

    pop = pop_input(knife, pistol, equipment, primary)
    # print(len(pop))
    matepool = roul_wheel(pop, len(pop), 10)
    #print(matepool)

    combination_matepool = two_combinations(matepool)
    #print(combination_matepool)

    mate_two_cross = []
    for i in range(len(combination_matepool)):
        mate_two_cross.append(two_pt_cross(combination_matepool[i][0], combination_matepool[i][1]))

    mate_two_cross = flatten(mate_two_cross)


    mate_two_cross = multi_bit_mut_rand(mate_two_cross, 1000)
    
    print(mate_two_cross)

