# Hill Climbing
def hill_climbing(n, X, gb):
    i, j, k, l = [random.randint(0, n-1) for i in range(4)]
    global i_pos, j_pos, k_pos, l_pos
    #print(i, j, k, l)
    pb = X[i][j][k][l]
    # print(pb)

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
                                # print('i1, j1, k1, l1:', i,
                                # ',', j, ',', k, ',', l)
                                pb = X[i][j][k][l]
                                # print(pb)
                                i_pos, j_pos, k_pos, l_pos = i, j, k, l

        count = count + 1
        if count > 100:
            break
    print('i, j, k, l:', i_pos, ',', j_pos, ',', k_pos, ',', l_pos)

    print('max:', pb)
