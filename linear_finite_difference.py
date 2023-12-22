import math

def lin_finit_diff(a,b,ya,yb,N,p,q,r):
    h = (b-a)/(N+1)
    x = a+h
    arr_a = [2+h**2*q(x)]
    arr_b = [-1+(h/2)*p(x)]
    arr_c = []
    arr_d = [-h**2*r(x)+(1+(h/2)*p(x))*ya]
    for i in range(2,N):
        x = a+i*h
        arr_a.append(2+h**2*q(x))
        arr_b.append(-1+(h/2)*p(x))
        arr_c.append(-1-(h/2)*p(x))
        arr_d.append(-h**2*r(x))
    x = b-h
    arr_a.append(2+h**2*q(x))
    arr_c.append(-1-(h/2)*p(x))
    arr_d.append(-h**2*r(x)+(1-(h/2)*p(x))*yb)

    arr_l = [arr_a[0]]
    arr_u = [arr_b[0]/arr_a[0]]
    arr_z = [arr_d[0]/arr_a[0]]

    for i in range(2,N):
        arr_l.append(arr_a[i-1]-arr_c[i-2]*arr_u[i-2])
        arr_u.append(arr_b[i-1]/arr_l[i-1])
        arr_z.append((arr_d[i-1]-arr_c[i-2]*arr_z[i-2])/arr_l[i-1])

    arr_l.append(arr_a[-1]-arr_c[-1]*arr_u[-1])
    arr_z.append((arr_d[-1]-arr_c[-1]*arr_z[-1])/arr_l[-1])

    arr_w = []
    for j in range(N+2):
        arr_w.append(0)
    arr_w[0] = ya
    arr_w[-1] = yb
    arr_w[-2] = arr_z[-1]

    for i in range(N-1,0,-1):
        arr_w[i] = arr_z[i-1]-arr_u[i-1]*arr_w[i+1]
    for i in range(N+2):
        print(a+i*h,arr_w[i])
    return("done")
def p(x):
    return -2/x

def q(x):
    return 2/x**2

def r(x):
    return math.sin(math.log(x))/x**2

def p2(x):
    return -(x+1)
def q2(x):
    return 2
def r2(x):
    return (1-x**2)*math.exp(-x)

def p3(x):
    return 0
def q3(x):
    return -4
def r3(x):
    return math.cos(x)

print(lin_finit_diff(1,2,1,2,9,p,q,r))
print(lin_finit_diff(0,1,1,0,9,p2,q2,r2))
print(lin_finit_diff(0,1,1,0,19,p2,q2,r2))
print(lin_finit_diff(0,math.pi/4,0,0,4,p3,q3,r3))




    
