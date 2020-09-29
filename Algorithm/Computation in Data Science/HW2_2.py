from __future__ import print_function
import numpy as np
import random


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

def walk(dis_table, goal_1):
    xb = []
    xb.append(dis_table[0][goal_1])
    pl = [goal_1] # The place have been travelled (i, j index)

    for _ in range(13):
        goal = random.randint(1,14)
        while goal == goal_1 or (goal in pl):
            goal = random.randint(1,14)
        pl.append(goal)

        xb.append(dis_table[goal_1][goal])
        goal_1 = goal
    xb.append(dis_table[goal_1][0]) # Back to Incheon
    #pl.append(0)
    total_len = Sum(xb)
    return pl, total_len

def route_count(dis_table, pl):
    xb = []
    xb.append(dis_table[0][pl[0]])
    for i in range(len(pl)-1):
        xb.append(dis_table[pl[i]][pl[i+1]])
    xb.append(dis_table[pl[len(pl)-1]][0])
    #print(xb)
    route_sum = Sum(xb)
    return route_sum

def find_neighbor(pl):
    pl_new = []
    move_1 = [pl[i]+1 for i in range(len(pl))]
    move_2 = [pl[i]-1 for i in range(len(pl))] 

    for i in move_1:
        for j in move_2:
            if i != j and i!=0 and i!=15 and j!=0 and j!=15 and (i not in pl_new) and (j not in pl_new):
                pl_new.append(i)
                pl_new.append(j)
    return pl_new


def rand_walk(dis_table):
    # The initial and final pos are both Incheon
    goal_1 = random.randint(1,14)
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
        
        goal_1 = random.randint(1,14)
        pl, total_len = walk(dis_table, goal_1)
        count = count + 1
    
    print(pl_best)
    print('Minimum Total:', pb_best)

    return pl_best, pb_best


def tabu_search(dis_table, pl_best, pb_best):
    pcur = pl_best
    pcur_fix = []
    for i in range(len(pcur)):
        pcur_fix.append(pcur[i])
    move = []
    OK_move, moveb = [], []
    route = []
    tabu = [0]*10

    count = 0
    
    while count <= 50:
        pnew = 0
        ptest = route_count(dis_table, pcur)

        for i in range(13):
            for j in range(13):
                if i != j:
                    move.append((i,j))
        
        for (i, j) in move:
            pcur_move = np.copy(pcur)
            tmp1, tmp2 = pcur[i], pcur[j]
            pcur_move[j], pcur_move[i] = tmp1, tmp2
            route.append(pcur_move)
            OK_move.append((i,j))
            

        for i in range(10):
            rout_dist = route_count(dis_table, route[i])
            if rout_dist < pb_best:
                pnew = rout_dist
                pb_best = rout_dist
                moveb = OK_move[i]

        count = count + 1 
    print(pb_best)
    print(moveb)
        
if __name__ == "__main__":
    

    dis_table= [[0 for x in range(15)] for y in range(15)] 
    Incheon = [0, 27, 335, 244, 41, 257, 33, 316, 186, 115, 304, 439, 102, 95, 275]
    Seoul   = [0, 0, 330, 237, 144, 268, 31, 307, 195, 113, 301, 453, 75, 69, 290]
    Busan   = [0, 0, 0, 95, 199, 193, 304, 54, 189, 221, 35, 291, 330, 271, 233]
    Daegu   = [0, 0, 0, 0, 117, 171, 212, 75, 130, 130, 130, 72, 324, 236, 191, 215]
    Daejeon = [0, 0, 0, 0, 0, 137, 114, 192, 61, 36, 167, 323, 175, 74, 171]
    Gwangju = [0, 0, 0, 0, 0, 0, 238, 222, 77, 173, 161, 186, 311, 162, 44]
    Suwon_si =[0, 0, 0, 0, 0, 0, 0, 284, 164, 84, 247, 423, 91, 83, 260]
    Ulsan   = [0, 0, 0, 0, 0, 0, 0, 0, 198, 205, 67, 341, 296, 266, 265]
    Jeonju  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 154, 263, 234, 97, 111]
    Cheong_si=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190, 359, 139, 74, 205]
    Changwon= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 275, 306, 237, 202]
    Jeju_si = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 498, 344, 165]
    Chuncheon=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 340]
    Hongsung =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180]
    Muan =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



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
    '''
    pl_best, pb_best = rand_walk(dis_table)

    tabu_search(dis_table, pl_best, pb_best)

