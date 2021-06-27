"""
ID: pranjal16
LANG: PYTHON3
TASK: sprime
"""

filein = open('sprime.in','r')
fileout = open('sprime.out','w')

text = filein.readlines()
N = int(text[0].strip())

filein.close()

# check if prime
def isprime(num):
    '''checks if the number is prime'''
    for i in range(3,int(num**0.5)+1,2):
        if not num % i:
            return False
    return True

# find sprimes
n = 1
sprimes = []
while n <= N:
    if n == 1:
        # append 1 digit primes
        sprimes.append(2)
        sprimes.append(3)
        sprimes.append(5)
        sprimes.append(7)
    else:
        oldprimes = sprimes[:]
        sprimes = []
        # check all odd last digits to see if a prime is possible
        for prime in oldprimes:
            for lastd in range(1,10,2):
                if isprime(10*prime + lastd):
                    sprimes.append(10*prime + lastd)
    n += 1

for prime in range(len(sprimes)):
    sprimes[prime] = str(sprimes[prime])

fileout.write('\n'.join(sprimes) + '\n')
