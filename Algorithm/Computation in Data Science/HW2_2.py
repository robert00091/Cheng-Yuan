import numpy
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


def rand_walk(dis_table):
    # The initial and final pos are both Incheon
    xb = []
    goal_1 = random.randint(1,14)
    xb.append(dis_table[0][goal_1])
    print(xb)
    pl = [goal_1] # The place have been travelled (i, j index)

    for _ in range(13):
        goal = random.randint(1,14)
        while goal == goal_1 or (goal in pl):
            goal = random.randint(1,14)
        pl.append(goal)
        #print(pl)

        xb.append(dis_table[goal_1][goal])
        print(xb)


        goal_1 = goal

    pl.append(0)
    print(pl)
        #count = count - 1
    






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

    for i in range(15):
        for j in range(15):
            print('{0:3d}'.format(dis_table[i][j]), end=' ')
        print('\n')

    rand_walk(dis_table)
