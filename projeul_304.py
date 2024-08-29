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



def num_ofPrimes(x):
    return int( x /math.log(x) )

##stt2 = int(1e14)
##end2 = int(1e14+4e7)

stt = int(float(input())) # 1e14
n = int(float(input())) # 1e5
mod = int(input())
t0 = time.time()

numOprimes = num_ofPrimes(stt)

##for iii in range(2):

Range = 0
while True:
    Range += 5
    if (num_ofPrimes(stt+Range) - numOprimes > n): # range is taken twice.. 
        break                                        # ..the estimated value
    
#~6e6
#Range*=(1+iii)  

stt1 = int(2)##
end1 = int((stt + Range)**0.5)+10

stt2 = stt
end2 = stt + Range

##stt1 = int(2)
##end1 = int(2e7)

##sieve1 = [0 for col in range(int(2e7))]
##sieve2 = [0 for col in range(int(4e7))]

sieve1 = [0 for col in range(end1)]
sieve2 = [0 for col in range(Range)]


##try:
t1 = time.time()
#print(t1-t0)

for i in range(stt1,end1):
    
    if sieve1[i]:continue

    for k in range(2*i, end1, i):
        sieve1[k] = i

    s2 = ( (stt2//i) + 1) * i - stt2
    e2 = (end2//i) * i - stt2
    

    if (e2 < Range-1):e2+=1
    
    for k in range(s2, e2, i):
        loop_started = True
        sieve2[k] = i
        
    try:   
        if (s2 == e2): sieve2[s2] = i
    except:
        continue
#except:
     
#     print("Error ", i)
t2 = time.time()
#print(t2-t1)

result = 0    
i=0
j=1

while ( i < n ):
    if ( not(sieve2[j]) ):
       i+=1
       result += fastFib(stt+j, mod)[0][1]
       result %= mod

    j+=1

print(result)

#t3 = time.time()
#print(t3-t2)
##if iii == 0:
##    sieve1_ = sieve1
##    sieve2_ = sieve2
##if iii == 1:
##    sieve1__ = sieve1
##    sieve2__ = sieve2

