import math
def trapezoidal(f,a,b,h,y0):
    x = a
    y = y0
    while x<b:
        y = y+(h/2)*(f(x,y)+f(x+h,y+h*f(x,y)))
        x = x+h
        print(x,y)
    return y
def f(x,y):
    return -x*y+4*(x/y)
print(trapezoidal(f,0,1,0.25,1))
