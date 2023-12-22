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
    return  1+y/x #1+(x-y)**2   #x*math.exp(3*x)-2*y
def adambash_3(w0,h,a,b,f):
    w1 = w0+h*heun(f,a,w0,h,a+h)
    print(a+h,w1)
    w2 = w1+h*heun(f,a+h,w1,h,a+2*h)
    print(a+2*h,w2)
    n = int((b-a)/h)
    for i in range(2,n):
        w = w2+(h/12)*(23*f(a+h*i,w2)-16*f(a+h*(i-1),w1)+5*f(a+h*(i-2),w0))
        w0 = w1
        w1 = w2
        w2 = w
        print(a+h*(i+1),w)
    return w
print(adambash_3(2,0.2,1,2,f))