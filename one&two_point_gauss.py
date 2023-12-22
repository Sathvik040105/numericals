#find integral of xsinx from 0 to pi/2 using one point gaussian quadrature
import math
def f(x):
    return x**3 + 5*x**2 + 1
def one_point_gauss(a,b):
    x_1 = (a+b)/2
    return (b-a)/2*f(x_1)
print(one_point_gauss(1,5))

def error_one_point_gauss(a,b):
    return -(b-a)**3/24*f(1)
print(error_one_point_gauss(1,5))

#find integral of xsinx from 0 to pi/2 using two point gaussian quadrature
import math  
def two_point_gauss(a,b):
    x_1 = (a+b)/2 - (b-a)/2/math.sqrt(3)
    x_2 = (a+b)/2 + (b-a)/2/math.sqrt(3)
    return ((b-a)/2)*(f(x_1)+f(x_2))
print(two_point_gauss(1,5))

def error_two_point_gauss(a,b):
    return -(b-a)**5/1920*f(1)
print(error_two_point_gauss(1,5))



