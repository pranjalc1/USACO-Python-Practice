'''
ID: pranjal16
LANG: PYTHON3
TASK: dualpal
'''

filein = open('dualpal.in','r')
fileout = open('dualpal.out','w')

text = filein.readlines()
nums = text[0].split()
N = int(nums[0])
S = int(nums[1])

filein.close()

def numinbase(B,n):
    '''finds n in base B'''
    largest = 0
    while B**largest <= n:
        largest += 1

    i = largest-1
    numinbaseb = ''
    while i > -1:
        numofipowers = n//(B**i)
        n -= numofipowers * B**i
        if numofipowers >= 10:
            numofipowers = chr(numofipowers + 55)
        numofipowers = str(numofipowers)
        numinbaseb += numofipowers
        i -= 1
    return numinbaseb

def is_palindrome(n):
    '''checks if a string is a palindrome'''
    return n == n[::-1]

S += 1
numlist = []
totalnums = 0

while totalnums < N:
    numpals = 0
    for base in range(2,11):
        if is_palindrome(numinbase(base,S)):
            numpals += 1
    if numpals >= 2:
        numlist.append(str(S))
        totalnums += 1
    S += 1

fileout.write('\n'.join(numlist) + '\n')
fileout.close()
