'''
Date: 2019/6/27
Author: Cheng-Yuan Wang
Title: Sparse Matrix
'''

# -*- coding: UTF-8 -*-
import numpy as np

def Input_fuc(row, col):
    count = 0
    matrix_A = []

    print('Enter the entries in rows:')

    for i in range(row):
        a = []
        for j in range(col):
            a.append(int(input()))
        matrix_A.append(a)

    for i in range(row):
        for j in range(col):
            print('{:>4d}'.format(matrix_A[i][j]), end = '|')
        print()

    return matrix_A

# Input sparse matrix
row = int(input('Enter the number of rows:'))
col = int(input('Enter the number of columns:'))
matrix_A = Input_fuc(row, col)

# Get the number of rows and columns
r = len(matrix_A)
c = len(matrix_A[0])

count = 0 # nonzero values

index = 0

#print(matrix_B)
for i in range(r):
    for j in range(c):
        if matrix_A[i][j] != 0:
            count += 1

matrix_B = np.zeros((count, 3))

for i in range(r):
    for j in range(c):
        if matrix_A[i][j] != 0:
            matrix_B[index][2] = matrix_A[i][j]
            matrix_B[index][1] = j+1
            matrix_B[index][0] = index+1
            index += 1
#print(matrix_B)


print('After processing the sparse matrix by 3-tuple method:')
print(matrix_B)

