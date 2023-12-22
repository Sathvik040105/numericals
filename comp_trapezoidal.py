#use composite trapezoidal rule to solve the integral of x^3 from 1 to 2
#use 4 subintervals
import math
def f(x):
    return x**3 + 5*x**2 + 1
def double_diff_f(x):
    return 6*x+10
def comp_trapezoidal(a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(1,n):
        sum=sum+f(a+i*h)
    return h*(f(a)+f(b))/2+h*sum
print(comp_trapezoidal(1,5,5))
print(comp_trapezoidal(1,5,10))

def error_comp_trapezoidal(a,b,n):
    h=(b-a)/n
    return -(h**2)*(b-a)/12*double_diff_f(1)
print(error_comp_trapezoidal(1,5,5))
print(error_comp_trapezoidal(1,5,10))