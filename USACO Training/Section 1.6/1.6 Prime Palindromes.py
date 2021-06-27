"""
ID: pranjal16
LANG: PYTHON3
TASK: pprime
"""

filein = open('pprime.in','r')
fileout = open('pprime.out','w')

text = filein.readlines()
a,b = text[0].split()
a,b = int(a),int(b)

filein.close()

# check if prime
def isprime(num):
    '''checks if the number is prime'''
    for i in range(3,int(num**0.5)+1,2):
        if not num % i:
            return False
    return True

# find palindromes (using hint for checking all possible cases)
pprimes = []

# 1 digit
pprimes.append(5)
pprimes.append(7)
# 2 digits
pprimes.append(11)

for a1 in range(1,10,2):
    for a2 in range(10):
        # 3 digits
        if isprime(101*a1 + 10*a2):
            pprimes.append(101*a1 + 10*a2)
        # no 4 digit pprimes since they have a multiple of 11
        if b > 10**4:
            for a3 in range(10):
                # 5 digits
                if isprime(10001*a1 + 1010*a2 + 100*a3):
                    pprimes.append(10001*a1 + 1010*a2 + 100*a3)
                # no 6 digit pprimes since they have a multiple of 11
                
                if b > 10**6:
                    for a4 in range(10):
                        # 7 digit
                        if isprime(1000001*a1 + 100010*a2 + 10100*a3 + 1000*a4):
                            pprimes.append(1000001*a1 + 100010*a2 + 10100*a3 + 1000*a4)
                        # no 8 digit pprimes since they have a multiple of 11

oldpprimes = pprimes[:]
oldpprimes.sort()
pprimes = []
for pprime in oldpprimes:
    if pprime in range(a,b+1):
        pprimes.append(str(pprime))

fileout.write('\n'.join(pprimes) + '\n')
