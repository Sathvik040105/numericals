def gauss_seidel(n,A,b,XO,tol,N):
    k = 1
    x = [0 for i in range(n)]
    while k<= N:
        for i in range(n):
            x[i] = (1/(A[i][i]))*(b[i]-sum(A[i][j]*x[j] for j in range(i))-sum(A[i][j]*XO[j] for j in range(i+1,n)))
        if all(abs(x[i]-XO[i])<tol for i in range(n)):
            return x
        k = k+1
        for i in range(n):
            XO[i] = x[i]
    return("Solution not found")

print(gauss_seidel(3,[[4,-1,1],[2,5,2],[1,2,4]],[8,3,11],[0,0,0],0.00001,100))