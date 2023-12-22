import math
def newton(p0,tol,N):
    i = 1
    x=[p0]
    y=[f(p0)]
    while i <= N:
        p = p0 - f(p0)/df(p0)
        if abs(p-p0) < tol:
            return math.exp(p)-p**3
        print("p",i,"=",p)
        i += 1
        p0 = p
    print('Method failed after',N,'iterations')

def f(x):
    return math.exp(x)-3*x**2

def df(x):
    return math.exp(x)-6*x

print(newton(3.5,1e-5,100))


