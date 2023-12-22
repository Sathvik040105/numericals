import math
def heun(f,a,b,h,y0):
    x = a
    y = y0
    while x<b:
        y = y+(h/4)*(f(x,y)+3*f(x+(2/3)*h,y+(2/3)*h*f(x+(1/3)*h,y+(1/3)*h*f(x,y))))
        x = x+h
        print(x,y)
    return y
def f(x,y):
    return 1+(x-y)**2
print(heun(f,2,3,0.2,1))
