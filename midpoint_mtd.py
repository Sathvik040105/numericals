#use midpoint method to solve the integral of sqrt(1+x^2) from 1 to 5
import math
def f(x):
    return math.sqrt(1+x**2)
def f2(x):
    return x**2+math.cos(x)
def midpoint(a,b,n):
    h=(b-a)/n
    return (b-a)*f2((a+b)/2)
    #return (b-a)*f2((a+b)/2)
#print(midpoint(1,5,1000))
print(midpoint(0,4,1000))

