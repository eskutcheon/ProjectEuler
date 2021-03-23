from numpy import log
from numpy import floor

'''
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?'''

# credit to source of formula goes to Sebastian Martiz Ruiz of Cadiz, Spain


'''def getLCM(k):
    LCM = 1
    for i in range(1,k+1):
        LCM = (LCM*i)//gcd(LCM,i)
    return LCM'''

# mathematical solution
def solution(nthPrime):
    finalPrime = 1
    tempSum = 0
    for i in range(1,2*(int(floor(nthPrime*log(nthPrime))))+1):
        innerSum = 0
        for j in range(2,i+1):
            innermostSum = 0
            for k in range(1,j+1):
                innermostSum += (2+((j-1)//k)-(j//k))
            innerSum += (1+(innermostSum//j))
        tempSum += (1-(innerSum//nthPrime))
    print(1+tempSum)

solution(10001)

