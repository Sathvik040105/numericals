#use comp_simpsom rule to solve the integral of x^3 from 1 to 2
#use 4 subintervals
import math
def f(x):
    return x**3 + 5*x**2 + 1
def diff4_f(x):
    return 6*x+10
def comp_simpson(a,b,n):
    h = (b-a)/n
    xI0 = f(a)+f(b)
    xI1 = 0
    xI2 = 0
    for i in range(1,n):
        x = a+i*h
        if i%2 == 0:
            xI2 = xI2 + f(x)
        else:
            xI1 = xI1 + f(x)
    return h/3*(xI0+2*xI2+4*xI1)
    # h = (b-a)/n
    # sum = 0
    # for i in range(1,n):
    #     sum = sum + f(a+i*h)
    # return h/3*(f(a)+f(b)+4*sum)
print(comp_simpson(1,5,5))
print(comp_simpson(1,5,10))

def error_comp_simpson(a,b,n):
    h = (b-a)/n
    return -(h**4)*(b-a)/180*diff4_f(1)
print(error_comp_simpson(1,5,5))
print(error_comp_simpson(1,5,10))
