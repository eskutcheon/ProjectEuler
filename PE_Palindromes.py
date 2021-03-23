# for Project Euler #4
import palindromicNumbers as pnums

pnumObj = pnums.PalindromeNumbers()
for i in range(900,1000):
    for j in range(900,1000):
        if(pnumObj.isPalindromic(i*j)):
            print(i*j)