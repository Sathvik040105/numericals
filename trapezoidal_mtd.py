#use trapezoidal rule to solve the integral of sqrt(1+x^2) from 1 to 5
import math
def f(x):
    return math.e**(x**2)
def double_diff_f(x):
    return 2*math.e**(x**2)*(2*x**2+1)
def trapezoidal(a,b,n):
    h=(b-a)
    return h*(f(a)+f(b))/2
print(trapezoidal(0,2,1000))

def error_trapezoidal(a,b,n):
    h=(b-a)/n
    return -(h**3)/12*double_diff_f(1)
print(error_trapezoidal(0,2,1000))