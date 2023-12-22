#use simpson method to find approx value of integral 1/(3-sqrt(x)) from 4 to 6
import math
def f1(x):
    return math.e**(x**2)
def f2(x):
    return x**3

def diff4_f1(x):
    return 2*math.e**(x**2)*(2*x**2+1)
def diff4_f2(x):
    return 6*math.cos(x)+math.cos(2*x)+math.cos(3*x)+math.cos(4*x)
def simpson_2(a,b,n):
    h = (b-a)/2
    x_1 = a + h
    sum = h/3*(f1(a)+f1(b)+4*f1(x_1))
    return sum
#print(simpson_2(4,6,1000))
print(simpson_2(0,2,1000))


def error_simpson_2(a,b,n):
    h=(b-a)/2
    return -(h**5)/90*diff4_f2(5)
print(error_simpson_2(0,2,1000))

#print(math.pi/3-simpson_2(0,math.pi/3,1000))