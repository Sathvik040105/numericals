import math
#use forward difference formula to approximate the derivative of lnx at x0 using h=0.1
def forward_diff(f,x0,h):
    return (f(x0+h)-f(x0))/h
print(forward_diff(math.log,1.8,0.1))
print(forward_diff(math.log,1.8,0.05))
print(forward_diff(math.log,1.8,0.01))
#use backward difference formula to approximate the derivative of lnx at x0 using h=0.1
def backward_diff(f,x0,h):
    return (f(x0)-f(x0-h))/h
print(backward_diff(math.log,1.8,0.1))
print(backward_diff(math.log,1.8,0.05))
print(backward_diff(math.log,1.8,0.01))
#use central difference formula to approximate the derivative of lnx at x0 using h=0.1
def central_diff(f,x0,h):
    return (f(x0+h)-f(x0-h))/(2*h)
print(central_diff(math.log,1.8,0.1))
print(central_diff(math.log,1.8,0.05))
print(central_diff(math.log,1.8,0.01))


def err(h):
    return h/(2*1.8**2)
print(err(0.1))
print(err(0.05))
print(err(0.01))
