import math
def heun(f,a,b,h,y0):
    x = a
    y = y0
    while x<b:
        y = y+(h/4)*(f(x,y)+3*f(x+(2/3)*h,y+(2/3)*h*f(x+(1/3)*h,y+(1/3)*h*f(x,y))))
        x = x+h
    return y

def fixedpoint(g,x0,tol):
    x1 = g(x0)
    N = 1
    for i in range(N):
        if abs(x1-x0)<tol:
            return x1
        x0 = x1
        x1 = x1 - (x1-g(x1))/(g(x1+tol)-g(x1))
    return x1

def f(x,y):
    return  1+(x-y)**2 #1+y/x #1+(x-y)**2   #x*math.exp(3*x)-2*y

def adammoult2(f,a,b,h,w0):
    w1 = heun(f,a,a+h,h,w0)
    print(a+h,w1)
    for i in range(1,int((b-a)/h)):
        w = fixedpoint(lambda w: w+h*(f(a+h*(i+1),w)+5*f(a+h*i,w)-f(a+h*(i-1),w))/12,w1,0.0001)
        w0 = w1
        w1 = w
        print(a+h*(i+1),w)
    return w

print(adammoult2(f,2,3,0.2,1))


    