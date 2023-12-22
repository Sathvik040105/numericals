#gauss_elimn using backward substitution
import numpy as np
import sys

from fractions import Fraction

# def print_aug(mat):
#     n0 = len(mat)
#     for i in range(0,n0):
#         I = ""
#         for k in range(0,n+1):
#             I += str(mat[i][k]) + "\t"
#             if j == n0-1:
#                 I += "|"
#         print(I)
#     print("")

def gauss_elemn(mat):
    num = len(mat)

    for i in range(0,num):
        max_el = abs(mat[i][i])
        max_row = i
        for k in range(i+1,num):
            if abs(mat[k][i])>max_el:
                max_el = abs(mat[k][i])
                max_row = k
        for k in range(i,num+1):
            tmp = mat[max_row][k]
            mat[max_row][k] = mat[i][k]
            mat[i][k] = tmp
        for k in range(i+1,num):
            c = -mat[k][i]/mat[i][i]
            for j in range(i,num+1):
                if i == j:
                    mat[k][j] = 0
                else:
                    mat[k][j] += c*mat[i][j]
    x = [0 for i in range(num)] 
    for i in range(num-1,-1,-1):
        x[i] = mat[i][num]/mat[i][i]
        for k in range(i-1,-1,-1):
            mat[k][num] -= mat[k][i]*x[i]
    return x

if __name__=="__main__":
    n = int(input())
    Aug_mat = [[0 for j in range(n+1)] for i in range(n)]
    print(Aug_mat)
    for j in range(0,n):
        I = list(map(Fraction,input().split(" ")))
        for i in range(3):
            Aug_mat[j][i] = I[i]

J = list(map(Fraction,input().split(" ")))

for j in range(0,n):
    Aug_mat[j][n] = J[j]

# print_aug(A_mat)

x = gauss_elemn(Aug_mat)

I = "Result: \t"
for j in range(0,n):
    I += str(x[j]) + "\t"
print(I)

