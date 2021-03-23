'''Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


def bruteForceSolution():
# Brute force method
    num = 2520 # known - first integer divisible by 1-10
    flag = False
    divisors = (11,13,14,15,16,17,18,19,20) # divisibility by these factors implies divisibility by their respective factors as well
    while flag is False:
        for i in divisors:
            # upon finding it's not divisible by some number in divisors, increment num and restart inner loop with next num
            if(num % i != 0):
                num += 1
                break
            if(i == 20): # if it hits this and it's true after the above break failed to execute, set flag to True
                flag = True
    print(num)



# mathematical solution uses the fact that the number in question will be divisible by the prime factorizations of 2-20
    # and thus can be found by division of the highest exponents recorded (e.g., 18 factors as 3**2 and 2**1 so the number in question being
    # a multiple of 3**2 AND a multiple of 'any exponent' of 2 means divisibility by 18)
def mathematicalSolution():
# Mathematical method
    primes = [2,3,5,7,11,13,17,19]
    primeExp = [0 for _ in range(8)]        # will store the max exponents of these prime factors found throughout the loops
    for i in range(2,21):                   # loop through numbers to be factored
        factored = [0 for _ in range(8)]    # will contain exponents for factorizations
        currentDiv = i                      # copies i to avoid decrementing
        while(currentDiv > 1):              # while the copy hasn't been
            for j in primes:
                if(currentDiv % j == 0):            # if currentDiv is a multiple of j
                    factored[primes.index(j)] += 1  # increment exponent count for that prime factor of i
                    currentDiv = currentDiv/j       # divide current div once factor is noted above
                    break                           # restart for inner loop with new currentDiv (tests the same prime factors without wasted effort)
        for k in range(len(primeExp)):      # once prime factors of i are found, the exponents are compared to those in primeExp and the highest is saved
            if(primeExp[k] < factored[k]):
                primeExp[k] = factored[k]
    finalNum = 1
    for i in range(len(primes)):
        finalNum *= (primes[i]**primeExp[i])    # final answer will be the product of all of the primes to the power of the highest exponent recorded for each prime
    print(finalNum)


mathematicalSolution()