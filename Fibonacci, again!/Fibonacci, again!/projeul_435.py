import time
import math


def matMul(A,B, mod, n=2):
    C = [[0 for col in range(n)] for row in range(n)]
    
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]       
    C = [[ (C[row][col]%mod) for col in range(n)] for row in range(n)]      
    return C
        
def fastFib(n, mod):
# returns a 2*2 matrix
    if n == 1:
        return [[1,1],[1,0]]
    if n == 2 :
        A = [[1,1],[1,0]]        
        return matMul(A,A,mod)

    if n%2 == 0 :
        A = fastFib(n//2, mod)
        return matMul(A,A,mod)

    else:
        A = fastFib(n//2, mod)
        A = matMul(A,A,mod)
        return matMul(A,[[1,1],[1,0]], mod)


n = int(float(input())) # 1e15
N = int(float(input())) # 100
mod = int(input())

def F(x,n,mod):
    b = x**2 + x - 1
    mb = mod*b
    
    B = pow(x,n+1, mb)
    A = (B*x)%mb
    
    final = fastFib(n,mb)[0][1]*A + fastFib(n+1,mb)[0][1]*B - x
    final %= mb
    test = (final%b == 0)
    final //= b
    return (final,test)

result = 0
for x in range(N+1):
#    Test = F(x,n,mod) 
    result += F(x,n,mod)[0]
    result %= mod
#    if not(Test[1]):print("error"); break
print(result)



