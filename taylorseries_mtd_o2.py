import math
def taylor(a,b,x0,y0,f,f1,h):
    print(x0,y0)
    while x0<=b:
        y0=y0+h*(taylor_term(f,f1,h,x0,y0))
        x0=x0+h
        print(x0,y0)
    return y0
def taylor_term(f,f1,h,x,y):
    return f(x,y)+f1(x,y)*h/2
def f(x,y):
    return math.sin(x)+math.exp(-x)#-x*y+4*x/y   #(y**2+y)/x    #math.sin(x)+math.exp(-x)    #y/x-(y**2/x**2)   #y-x**2+1
def f1(x,y):
    return math.cos(x)-math.exp(-x)#-y+x**2*y-(4*x**2/y)+(4*y+4*x**2*y-(16*x*x/y))/y**2   #(2*y*(y+y**2))/x**2      #math.cos(x)-math.exp(-x)    (y/x**2)-(y**2/x**3)-(y/x**2)-2*y+2*(y**2/x**3)   #y-x**2+1-2*x
print(taylor(0,1,0,0,f,f1,0.5))
