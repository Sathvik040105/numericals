#use linear shooting method to solve the boundary value problem
import math
def linear_shooting_runga(a,b,ya,yb,N,p,q,r,f):
    h = (b-a)/N
    u10 = [ya]
    u20 = [0]
    v10 = [0]
    v20 = [1]
    for i in range(N):
        x = a+i*h
        k11 = h*(u20[i])
        k12 = h*(p(x)*u20[i]+q(x)*u10[i]+r(x))
        k21 = h*(u20[i]+k12/2)
        k22 = h*(p(x+h/2)*(u20[i]+k12/2)+q(x+h/2)*(u10[i]+k11/2)+r(x+h/2))
        k31 = h*(u20[i]+k22/2)
        k32 = h*(p(x+h/2)*(u20[i]+k22/2)+q(x+h/2)*(u10[i]+k21/2)+r(x+h/2))
        k41 = h*(u20[i]+k32)
        k42 = h*(p(x+h)*(u20[i]+k32)+q(x+h)*(u10[i]+k31)+r(x+h))
        u10.append(u10[i]+(k11+2*k21+2*k31+k41)/6)
        u20.append(u20[i]+(k12+2*k22+2*k32+k42)/6)
        k_11 = h*v20[i]
        k_12 = h*(p(x)*v20[i]+q(x)*v10[i])
        k_21 = h*(v20[i]+k_12/2)
        k_22 = h*(p(x+h/2)*(v20[i]+k_12/2)+q(x+h/2)*(v10[i]+k_11/2))
        k_31 = h*(v20[i]+k_22/2)
        k_32 = h*(p(x+h/2)*(v20[i]+k_22/2)+q(x+h/2)*(v10[i]+k_21/2))
        k_41 = h*(v20[i]+k_32)
        k_42 = h*(p(x+h)*(v20[i]+k_32)+q(x+h)*(v10[i]+k_31))
        v10.append(v10[i]+(k_11+2*k_21+2*k_31+k_41)/6)
        v20.append(v20[i]+(k_12+2*k_22+2*k_32+k_42)/6)
    w10 = ya
    w20 = (yb-u10[-1])/v10[-1]
    print(a,w10,w20,f(a))
    for i in range(1,N):
        W1 = u10[i]+w20*v10[i]
        W2 = u20[i]+w20*v20[i]
        x = a+i*h
        print(x,W1,W2,f(x))
    return("done")
# def p(x):
#     return -2/x
# def q(x):
#     return 2/x**2
# def r(x):
#     return math.sin(math.log(x))/x**2
# def f(x):
#     return 1.1392070132*x+(-0.03920701320)/x**2-(0.3)*(math.sin(math.log(x)))-(0.1)*(math.cos(math.log(x)))

# print(linear_shooting_runga(1,2,1,2,10,p,q,r,f))

def p(x):
    return 0
def q(x):
    return 4
def r(x):
    return -4*x
def f(x):
    return (math.exp(2)*(math.exp(2*x)-math.exp(-2*x))/(math.exp(4)-1))+x

print(linear_shooting_runga(0,1,0,2,4,p,q,r,f))

def linear_shooting_newton(a,b,ya,yb,N,tol,M,f,fy1,fy2,z):
    h = (b-a)/N
    k = 1
    TK = (yb-ya)/(b-a)
    while k<=M:
        w10 = [ya]
        w20 = [TK]
        u1 = 0
        u2 = 1 
        for i in range(1,N):
            x = a+(i-1)*h
            k11 = h*w20[i-1]
            k12 = h*f(x,w10[i-1],w20[i-1])
            k21 = h*(w20[i-1]+k12/2)
            k22 = h*f(x+h/2,w10[i-1]+k11/2,w20[i-1]+k12/2)
            k31 = h*(w20[i-1]+k22/2)
            k32 = h*f(x+h/2,w10[i-1]+k21/2,w20[i-1]+k22/2)
            k41 = h*(w20[i-1]+k32)
            k42 = h*f(x+h,w10[i-1]+k31,w20[i-1]+k32)
            w10.append(w10[i-1]+(k11+2*k21+2*k31+k41)/6)
            w20.append(w20[i-1]+(k12+2*k22+2*k32+k42)/6)
            k_11 = h*u2
            k_12 = h*(fy2(x,w10[i-1],w20[i-1])*u2+fy1(x,w10[i-1],w20[i-1])*u1)
            k_21 = h*(u2+k_12/2)
            k_22 = h*(fy2(x+h/2,w10[i-1],w20[i-1])*(u2+k_12/2)+fy1(x+h/2,w10[i-1],w20[i-1])*(u1+k_11/2))
            k_31 = h*(u2+k_22/2)
            k_32 = h*(fy2(x+h/2,w10[i-1],w20[i-1])*(u2+k_22/2)+fy1(x+h/2,w10[i-1],w20[i-1])*(u1+k_21/2))
            k_41 = h*(u2+k_32)
            k_42 = h*(fy2(x+h,w10[i-1],w20[i-1])*(u2+k_32)+fy1(x+h,w10[i-1],w20[i-1])*(u1+k_31))
            u1 = u1+(k_11+2*k_21+2*k_31+k_41)/6
            u2 = u2+(k_12+2*k_22+2*k_32+k_42)/6
        if abs(w10[-1]-yb)<= tol:
            for i in range(N):
                x = a+i*h
                print(x,w10[i],w20[i],z(x))
            return("done")
        TK = TK-(w10[-1]-yb)/u1
        k = k+1
    return("failed")

def f(x,y1,y2):
    return (1/8)*(32+2*(x**3)-y1*y2)
def fy1(x,y1,y2):
    return -(1/8)*y2
def fy2(x,y1,y2):
    return -(1/8)*y1
def z(x):
    return x**2+16/x

print(linear_shooting_newton(1,3,17,43/3,20,0.00001,10,f,fy1,fy2,z))
