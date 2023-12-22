import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/(1+x**2)

def interpolate(x,n):
    arrx = []
    for i in range(-1,1,2/n):
        arrx.append(i)
    print(arrx)
    Q = []
    for j in range(n):
        Q[j] = f(arrx[j])
    for i in range(len(arrx)):
        for j in range(i):
            return (((x-arrx[i-j])*Q[i][j-1])-(x-arrx[i])*Q[i-1][j-1])/(arrx[i]-arrx[i-j])

print(interpolate(3,4))
