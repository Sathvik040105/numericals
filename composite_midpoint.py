#use composite midpoint method to find the definite integral of x^3+5x^2+1 from 1 to 5
#use 100 rectangles
def f(x):
    return x**3 + 5*x**2 + 1
a=1
b=5
n=10
h=(b-a)/n
integral = 0
for i in range(n):
    integral += h*f(a+i*h+h/2)
print("the integral is",integral)

