from os import rename
from unittest import result


def Multiply(A,B):
    result = [ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for Columns
        for j in range(len(B[0])):
            #for Rows of matrix B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for p in result:
        print(p)
    return 0

A = [ [1, 2, 3], [6, 7, 8], [8, 10, 11] ]
B = [ [2, 4, 5], [4, 6, 7], [6, 19, 11] ]

print("Result: ")
Multiply(A,B)