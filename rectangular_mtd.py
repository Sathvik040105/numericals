# use rectangular method to find the definite integral of sqrt(1+x^2) from 1 to 5
#use 100 rectangles
def f(x):
    return (1+x**2)**0.5
a=1
b=5
n=10000
h=(b-a)
integral = h*f(a)
print("the integral is",integral)                                                                                  