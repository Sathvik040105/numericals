# use rungekutta method to approximate the solution of the initial value problem dy/dx=2x+3y, y(0)=1
import math

def rungekutta(f,x0,y0,h,x_target):
    x = x0 
    y = y0
    while x<x_target:
        k1 = h*f(x,y)
        k2 = h*f(x+h/2,y+k1/2)
        y = y+k2
        x = x+h
        print(x,y)
    return y

def f(x,y):
    return 1+(x-y)**2

print(rungekutta(f,2,1,0.1,2.2))
print(2.2+(1/(1-(2.2))))
#path: rungekutte_o2.py
