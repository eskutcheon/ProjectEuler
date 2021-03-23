# quick script for the project Euler problem #3
import math
def largestPrimeFactor(num):
        # most efficient method using brute force even with good choice of starting point:
    maxprime = -1
    while(num % 2 == 0):
        print(2,', ')
        num /= 2 # once the loop exits, there are no more prime factors of 2 and the number must be odd then so a step size of 2 is possible
    for i in range(3,int(math.sqrt(num))+1,2): # upper bound of sqrt(num) since this would be the next largest factor if applicable
        #print('not prime: %d' % (i))
        while(num % i == 0):
            maxprime = i
            num /= i
    if num > 2:
        maxprime = num
    return maxprime

print(largestPrimeFactor(600851475143))
