# primes.py
# Author: Kevin

primes = []
upto = 101

for candidate in range(2, upto):
    #print(candidate)
    isPrime = True
    for divisor in range(2, candidate):
        if(candidate%divisor == 0):#
            isPrime = False
            break
    if isPrime:
        primes.append(candidate)

print(primes)