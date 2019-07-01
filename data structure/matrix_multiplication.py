'''
Date: 2019/6/27
Author: Cheng-Yuan Wang
Title: Multiplication of Matrix
'''

# -*- coding: UTF-8 -*-

def Input_func(row1, col1, row2, col2):

    # Initialize Matrix
    matrix_A = []

    print('Enter the entries in rows:')

    # For users input
    for i in range(row1):
        a = []
        for j in range(col1):
            a.append(int(input()))
        # print(a)
        matrix_A.append(a)

    # For printing the desired matrix
    print('Matrix_A:')
    for i in range(row1):
        for j in range(col1):
            print(matrix_A[i][j], end=' ')
        print()


    # Initialize Matrix
    matrix_B = []

    print('Enter the entries in rows:')

    # For users input
    for i in range(row2):
        a = []
        for j in range(col2):
            a.append(int(input()))
        # print(a)
        matrix_B.append(a)

    # For printing the desired matrix
    print('Matrix_B:')
    for i in range(row2):
        for j in range(col2):
            print(matrix_B[i][j], end=' ')
        print()

    return matrix_A, matrix_B

# User inputs matrix
row1 = int(input('A,Enter the number of rows:'))
col1 = int(input('A,Enter the number of columns:'))
row2 = int(input('B,Enter the number of rows:'))
col2 = int(input('B,Enter the number of columns:'))

aryA, aryB = Input_func(row1,col1,row2,col2)
#print(aryA)
#print(aryB)

X = len(aryA); Y = len(aryB); Z = len(aryB[0])
aryC =[]

for i in range(X):
    a = []
    for j in range(Z):
        total = 0 # initialize the value
        for k in range(Y):
            total += aryA[i][k] * aryB[k][j]
        a.append(total)
    aryC.append(a)
    #print(aryC)

print('After multiplying:')
for i in range(X):
    for j in range(Z):
        print('{:>4d}'.format(aryC[i][j]), end = '|')
    print()

