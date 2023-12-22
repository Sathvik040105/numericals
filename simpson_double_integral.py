import math
def f(x,y):
    return math.log(x+2*y)
def diff4_f(x,y):
    return (-6)/(x+2*y)**4

def double_simpson(a,b,c,d,m,n):
    h = (b-a)/n
    j1 = 0 #even
    j2 = 0 #even
    j3 = 0 #odd
    for i in range(0,n+1):
        x = a+i*h
        hx = (d-c)/m
        k1 = f(x,c)+f(x,d)
        k2 = 0
        k3 = 0
        for j in range(1,m):
            y = c+j*hx
            Q = f(x,y)
            if j%2 == 0:
                k2 = k2 + Q
            else:
                k3 = k3 + Q
        L = (k1+2*k2+4*k3)*hx/3
        if i == 0 or i == n:
            j1 = j1 + L
        elif i%2 == 0:
            j2 = j2 + L
        else:
            j3 = j3 + L
    return h/3*(j1+2*j2+4*j3)

print(double_simpson(1.4,2.0,1.0,1.5,4,2))

def error_double_simpson(a,b,c,d,m,n):
    h = (b-a)/n
    hx = (d-c)/m
    return -(h**4)*(b-a)*(d-c)/180*diff4_f(1,1)
print(error_double_simpson(1.4,2.0,1.0,1.5,4,2))

