from __future__ import print_function
from itertools import combinations 
import numpy as np
import random
import math


'''            
            Incheon   Seoul   Busan  Daegu  Daejeon   Gwangju   Suwon-si   Ulsan   Jeonju   Cheongju-si   Changwon   Jeju-si   Chuncheon   Hongsung    Muan
           |------------------------------------------------------------------------------------------------------------------------------------------------
Incheon    | X         27      335    244      41       257        33       316      186        115          304       439         102       95        275
Seoul      |            X      330    237     144       268        31       307      195        113          301       453          75       69        290
Busan      |                     X     95     199       193       304        54      189        221           35       291         330      271        233
Daegu      |                            X     117       171       212        75      130        130           72       324         236      191        215
Daejeon    |                                    X       137       114       192       61         36          167       323         175       74        171
Gwangju    |                                              X       238       222       77        173          161       186         311      162         44
Suwon-si   |                                                        X       284      164         84          274       423          91       83        260
Ulsan      |                                                                  X      198        205           67       341         296      266        265
Jeonju     |                                                                           X         96          154       263         234       97        111
Cheongju-si|                                                                                      X          190       359         139       74        205
Changwon   |                                                                                                   X       275         306      237        202 
Jeju-si    |                                                                                                             X         498      344        165
Chuncheon  |                                                                                                                         X      170        340
Hongsung   |                                                                                                                                  X        180
Muan       |                                                                                                                                             X

'''


def Sum(xb):
    total = 0
    for i in range(len(xb)):
        total = total + xb[i]
    return total


def plot(x, y, j, k):
    return 0


def walk(dis_table, goal_1):
    xb = []
    xb.append(dis_table[0][goal_1])
    pl = [goal_1]  # The place have been travelled (i, j index)

    for _ in range(13):
        goal = random.randint(1, 14)
        while goal == goal_1 or (goal in pl):
            goal = random.randint(1, 14)
        pl.append(goal)

        xb.append(dis_table[goal_1][goal])
        goal_1 = goal
    xb.append(dis_table[goal_1][0])  # Back to Incheon
    # pl.append(0)
    total_len = Sum(xb)
    return pl, total_len


def route_count(dis_table, pl):
    xb = []
    xb.append(dis_table[0][pl[0]])
    for i in range(len(pl)-1):
        xb.append(dis_table[pl[i]][pl[i+1]])
    xb.append(dis_table[pl[len(pl)-1]][0])
    # print(xb)
    route_sum = Sum(xb)
    return route_sum


def find_neighbor(pl):
    pl_new = []
    move_1 = [pl[i]+1 for i in range(len(pl))]
    move_2 = [pl[i]-1 for i in range(len(pl))]

    for i in move_1:
        for j in move_2:
            if i != j and i != 0 and i != 15 and j != 0 and j != 15 and (i not in pl_new) and (j not in pl_new):
                pl_new.append(i)
                pl_new.append(j)

    return pl_new


def tabu_move(dis_table, pcur, pb_best, tabu):
    route, move = [], []
    OK_move, moveb, route_move = [], [], []

    for i in range(14):
        for j in range(14):
            if i != j:
                move.append((i, j))

    for (i, j) in move:
        if (i, j) not in tabu:
            pcur_move = np.copy(pcur)
            tmp1, tmp2 = pcur[i], pcur[j]
            pcur_move[j], pcur_move[i] = tmp1, tmp2
            route.append(pcur_move)
            OK_move.append((i, j))

    for i in range(len(route)):
        rout_dist = route_count(dis_table, route[i])
        #print(rout_dist, ',', OK_move[i])
        if rout_dist < pb_best:
            #pnew = rout_dist
            pb_best = rout_dist

            if moveb == OK_move[i]:  # Take the first move if move are the same
                OK_move[i] = moveb
                route_move = route[i]
            else:
                moveb = OK_move[i]
                route_move = route[i]
    # print(route_move)
    return route_move, pb_best, moveb


def rand_walk(dis_table):
    # The initial and final pos are both Incheon
    goal_1 = random.randint(1, 14)
    pl, total_len = walk(dis_table, goal_1)
    #print('Total length:', total_len)
    pb_best = total_len
    pl_best = pl

    count = 0
    while count <= 100:

        pl_new = find_neighbor(pl)

        min_total = route_count(dis_table, pl_new)
        if min_total < pb_best:
            pb_best = min_total
            pl_best = pl_new

        goal_1 = random.randint(1, 14)
        pl, total_len = walk(dis_table, goal_1)
        count = count + 1

    print(pl_best)
    print('Minimum Total:', pb_best)

    return pl_best, pb_best


def tabu_search(dis_table, pl_best, pb_best):
    pcur = pl_best
    tabu, route_move = [], pcur
    pl_best = []
    count = 0

    while count <= 100:
        pnew = 0
        ptest = route_count(dis_table, pcur)
        route_move, pb_best, moveb = tabu_move(
            dis_table, route_move, ptest, tabu)
        tabu.append(moveb)

        if len(tabu) > 10:
            tabu.pop(9)

        count = count + 1
    for i in range(len(route_move)):
        pl_best.append(route_move[i])

    print(pl_best)
    print('Minimum Total:', pb_best)

    return pl_best, pb_best
    # print(tabu)


def simu_annealing(dis_table, pl_best, pb_best):
    pl, pcur = pl_best, pb_best
    pl_best = pl
    pbest = pcur
    T = 10
    t = 0
    c = 1-(t/T)

    count = 0
    while count <= 10:

        while t <= 10000:

            pl_new = find_neighbor(pl)
            dE = route_count(dis_table, pl_new) - route_count(dis_table, pl)
            if dE <= 0:
                pl = pl_new
                pcur = route_count(dis_table, pl_new)
                if pcur < pbest:
                    pbest = pcur

            else:  # dE > 0: using the Metropolis criterion
                T = T * c
                rv = random.uniform(0, 1)
                if rv < math.exp(-dE/T):
                    pcur = route_count(dis_table, pl_new)
            pl, total_len = walk(dis_table, random.randint(1, 14))
            t = t + 1

        count = count + 1
    print(pl)
    print('Minimum Total:', pbest)


def hill_climb(dis_table, pl_best, pb_best):
    # The initial and final pos are both Incheon
    pl, total_len = pl_best, pb_best
    #print('Total length:', total_len)
    pb_best = total_len
    pl_best = pl

    count = 0
    while count <= 100:

        pl_new = find_neighbor(pl)

        min_total = route_count(dis_table, pl_new)
        if min_total < pb_best:
            pb_best = min_total
            pl_best = pl_new

        #pl, total_len = walk(dis_table, goal_1)
        count = count + 1

    print(pl_best)
    print('Minimum Total:', pb_best)


def phero_evap(phero_memory):
    p = 0.5
    for i in range(len(phero_memory)):
        for j in range(len(phero_memory[i])):
            phero_memory[i][j] = phero_memory[i][j] * (1-p)
    return phero_memory

def roulette_wheel(phero_memory, l):
    P = [[0 for j in range(n)] for i in range(n)]
    #print(phero_memory[0])
    for i in range(n):
        total = sum(phero_memory[i])
        for j in range(n):
            p = pow(phero_memory[i][j], l)/total
            P[i][j] = P[i][j] + p*j

    return P

def aco(dis_table, N, n, t):
    # a: pheromone
    a = [1 for i in range(n)]
    l = 1
    f_best = 999999
    f_worst = -999999
    global_best = 0
    global_best_pl = []

    c = 2

    phero_memory = [[1 for j in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==j: phero_memory[i][j] =0
    
    #print(phero_memory)

    while l <= t:
        pl = []  # place has been visited
        #phero = [1 for i in range(n)]
        P = [0 for i in range(n)]
        total = sum(a)
        for j in range(n):
            p = pow(a[j], l)/total
            # Probability of pheromone corresponding to each place in the ant's path
            P[j] = P[j] + p*j
        # print(P)
        #phero_memory = phero_evap(phero_memory)
        for i in range(N):
            init = random.randint(1, 14)
            pl.append(init)

            while(len(pl) < n):
                j = random.randint(1, 14)
                if j not in pl:
                    pl.append(j)

            #print("ant", i+1, ":", pl)
            total_route = route_count(dis_table, pl)
            #print('Total route:', total_route)
            
            delta_phero = 1/total_route
            
            for i in range(len(pl)-1):
                before = pl[i]
                after = pl[i+1]

                phero_memory[before][after] = phero_memory[before][after]  + delta_phero
                phero_memory[after][before] = phero_memory[before][after]

                phero_memory[0][pl[0]] = phero_memory[0][pl[0]] + delta_phero
                phero_memory[pl[0]][0] = phero_memory[pl[0]][0] + delta_phero
                phero_memory[0][pl[13]] = phero_memory[0][pl[13]] + delta_phero
                phero_memory[pl[13]][0] = phero_memory[pl[13]][0] + delta_phero
                #print(phero_memory)

            P = roulette_wheel(phero_memory, l)
            #print(P)

            pl_new = []
            while len(pl_new) <= 13: 
                for i in range(n):
                    r = random.uniform(0, 1)
                    for j in range(1, n):
                        if P[i][j-1] <= r <= P[i][j] and j not in pl_new:
                            pl_new.append(j)
                        
                        if len(pl_new) == 13:
                            for k in range(1,15):
                                if k not in pl_new:
                                    pl_new.append(k)

            
            if route_count(dis_table, pl_new) < f_best:
                global_best_pl = pl_new
                f_best = route_count(dis_table, pl_new)
            if route_count(dis_table, pl_new) > f_worst:
                f_worst = route_count(dis_table, pl_new)

            pl = []

        global_best = f_best
        #phero_evap(phero_memory)
        l = l+1
    print(global_best_pl)
    return global_best

if __name__ == "__main__":

    dis_table = [[0 for x in range(15)] for y in range(15)]
    Incheon = [0, 27, 335, 244, 41, 257, 33,
               316, 186, 115, 304, 439, 102, 95, 275]
    Seoul = [0, 0, 330, 237, 144, 268, 31,
             307, 195, 113, 301, 453, 75, 69, 290]
    Busan = [0, 0, 0, 95, 199, 193, 304, 54, 189, 221, 35, 291, 330, 271, 233]
    Daegu = [0, 0, 0, 0, 117, 171, 212, 75,
             130, 130, 130, 72, 324, 236, 191, 215]
    Daejeon = [0, 0, 0, 0, 0, 137, 114, 192, 61, 36, 167, 323, 175, 74, 171]
    Gwangju = [0, 0, 0, 0, 0, 0, 238, 222, 77, 173, 161, 186, 311, 162, 44]
    Suwon_si = [0, 0, 0, 0, 0, 0, 0, 284, 164, 84, 247, 423, 91, 83, 260]
    Ulsan = [0, 0, 0, 0, 0, 0, 0, 0, 198, 205, 67, 341, 296, 266, 265]
    Jeonju = [0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 154, 263, 234, 97, 111]
    Cheong_si = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190, 359, 139, 74, 205]
    Changwon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 275, 306, 237, 202]
    Jeju_si = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 498, 344, 165]
    Chuncheon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 340]
    Hongsung = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180]
    Muan = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(15):
        dis_table[0][i] = dis_table[i][0] = Incheon[i]
        dis_table[1][i] = dis_table[i][1] = Seoul[i]
        dis_table[2][i] = dis_table[i][2] = Busan[i]
        dis_table[3][i] = dis_table[i][3] = Daegu[i]
        dis_table[4][i] = dis_table[i][4] = Daejeon[i]
        dis_table[5][i] = dis_table[i][5] = Gwangju[i]
        dis_table[6][i] = dis_table[i][6] = Suwon_si[i]
        dis_table[7][i] = dis_table[i][7] = Ulsan[i]
        dis_table[8][i] = dis_table[i][8] = Jeonju[i]
        dis_table[9][i] = dis_table[i][9] = Cheong_si[i]
        dis_table[10][i] = dis_table[i][10] = Changwon[i]
        dis_table[11][i] = dis_table[i][11] = Jeju_si[i]
        dis_table[12][i] = dis_table[i][12] = Chuncheon[i]
        dis_table[13][i] = dis_table[i][13] = Hongsung[i]
        dis_table[14][i] = dis_table[i][14] = Muan[i]
    '''
    for i in range(15):
        for j in range(15):
            print('{0:3d}'.format(dis_table[i][j]), end = ' ')
        print('\n')
    

    print("Random Walk:")
    pl_best, pb_best = rand_walk(dis_table)

    print("\nTabu Search:")
    pl_best1, pb_best1 = tabu_search(dis_table, pl_best, pb_best)


    print("\nSimulated Annealing:")
    simu_annealing(dis_table, pl_best, pb_best)

    print("\nHill Climbing:")
    hill_climb(dis_table, pl_best1, pb_best1)

    '''

    print("Ant Colony Optimization:")

    N, n, t = 5, 14, 5
    print('global best route:', aco(dis_table, N, n, t))
