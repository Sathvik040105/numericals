# import math
# def f(x,y):
#     return math.log(x+2*y)
# def diff4_f(x,y):
#     return (-6)/(x+2*y)**4
# def r(x,y):
#     if x==1 and y==1:
#         return 0
#     elif x==1 and y==2:
#         return 0
#     elif x==2 and y==1:
#         return -1/math.sqrt(3)
#     elif x==2 and y==2:
#         return 1/math.sqrt(3)
# def c(x,y):
#     if x==1 and y == 1:
#         return 1
#     elif x==2 and y==1:
#         return 1
#     elif x==2 and y==2:
#         return -1/3
    
# def gauss_double(a,b,c,d,m,n):
#     h1 = (b-a)/2
#     h2 = (b+a)/2
#     J = 0
#     for i in range(1,m+1):
#         Jx = 0
#         x = h1*r(m,i)+h2
#         k1 = (d-c)/2
#         k2 = (d+c)/2
#         for j in range(1,n+1):
#             y = k1*r(n,j)+k2
#             Q = f(x,y)
#             Jx = Jx + c(n,j)*Q
#         J = J + Jx*k1*c(m,i)
#     return J*h1
# print(gauss_double(1.4,2.0,1.0,1.5,2,2))

#use gauss_double to solve the integral of ln(x+2y) from 1.4 to 2.0 and 1.0 to 1.5
#use 2 subintervals
import math

def f(x, y):
    return math.log(x + 2 * y)

def diff4_f(x, y):
    return (-6) / (x + 2 * y) ** 4

def r(x, y):
    if x == 1 and y == 1:
        return 0
    elif x == 2 and y == 1:
        return -1 / math.sqrt(3)
    elif x == 2 and y == 2:
        return 1 / math.sqrt(3)
def c(x, y):
    if x == 1 and y == 1:
        return 1
    elif x == 2 and y == 1:
        return 1
    elif x == 2 and y == 2:
        return 1

def gauss_double(a, b, c, d, m, n):
    h1 = (b - a) / 2
    h2 = (b + a) / 2
    J = 0
    for i in range(1, m + 1):
        Jx = 0
        x = h1 * r(m, i) + h2
        k1 = (d - c) / 2
        k2 = (d + c) / 2
        for j in range(1, n + 1):
            y = k1 * r(n, j) + k2
            Q = f(x, y)
            Jx = Jx + Q * c(n, j)
        J = J + Jx * k1 * c(m, i)
    return J * h1 * h2

print(gauss_double(1.4, 2.0, 1.0, 1.5, 2, 2))

