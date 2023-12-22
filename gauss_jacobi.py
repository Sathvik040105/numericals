def gauss_jacobi(n,A,b,XO,tol,N):
    k = 1
    x = [0 for i in range(n)]
    while k<= N:
        for i in range(n):
            x[i] = (1/(A[i][i]))*(b[i]-sum(A[i][j]*XO[j] for j in range(n) if j!=i))
        if all(abs(x[i]-XO[i])<tol for i in range(n)):
            return x
        k = k+1
        for i in range(n):
            XO[i] = x[i]
    return("Solution not found")

print(gauss_jacobi(3,[[1,2,3],[2,-1,2],[3,1,-2]],[5,1,-1],[0,0,0],0.00001,100))



