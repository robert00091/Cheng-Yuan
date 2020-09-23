# Random Walk
def rand_walk(n, X, gb):
    i, j, k, l = [random.randint(0, n-1) for i in range(4)]
    global i_pos, j_pos, k_pos, l_pos
    #print(i, j, k, l)
    pb = X[i][j][k][l]
    # print(pb)
    pb_max = 0

    count = 0
    while pb < 0.95*gb or count < 10:
        i_next, j_next, k_next, l_next = [
            i+1, i-1], [j+1, j-1], [k+1, k-1], [l+1, l-1]

        for i in i_next:
            for j in j_next:
                for k in k_next:
                    for l in l_next:
                        if 0 <= i < n and 0 <= j < n and 0 <= k < n and 0 <= l < n:
                            if X[i][j][k][l] > pb:
                                pb = X[i][j][k][l]
                                if pb > pb_max:
                                    pb_max = pb
                                i_pos, j_pos, k_pos, l_pos = i, j, k, l
        # randomize the next initial state
        i, j, k, l = [random.randint(0, n-1) for i in range(4)]
        count = count + 1
        if count > 100:
            break
    print('i, j, k, l:', i_pos, ',', j_pos, ',', k_pos, ',', l_pos)
 
    print('max:', pb_max)
