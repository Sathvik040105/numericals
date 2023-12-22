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
    return  x*math.exp(3*x)-2*y#1+y/x #1+(x-y)**2   #x*math.exp(3*x)-2*y
def adambash_2(w0,h,a,b,f):
    w1 = w0+h*rungekutta(f,a,w0,h,a+h)
    n = int((b-a)/h)
    for i in range(1,n):
        w = w1+(h/2)*(3*f(a+h*i,w1)-f(a+h*(i-1),w0))
        w0 = w1
        w1 = w
        print(a+h*(i+1),w)
    return w
print(adambash_2(0,0.2,0,1,f))





