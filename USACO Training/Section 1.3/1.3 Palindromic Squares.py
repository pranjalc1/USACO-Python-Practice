'''
ID: pranjal16
LANG: PYTHON3
TASK: palsquare
'''

filein = open('palsquare.in','r')
fileout = open('palsquare.out','w')

B = int(filein.readlines()[0].strip())

filein.close()

def numinbase(B,N):
    '''finds N in base B'''
    largest = 0
    while B**largest <= N:
        largest += 1

    i = largest-1
    numinbaseb = ''
    while i > -1:
        numofipowers = N//(B**i)
        N -= numofipowers * B**i
        if numofipowers >= 10:
            numofipowers = chr(numofipowers + 55)
        numofipowers = str(numofipowers)
        numinbaseb += numofipowers
        i -= 1
    return numinbaseb

def is_palindrome(N):
    '''checks if a string is a palindrome'''
    return N == N[::-1]

possiblepairs = []
for n in range(1,301):
    square = n**2
    squareinb = numinbase(B,square)
    if is_palindrome(squareinb):
        possiblepairs.append(numinbase(B,n) + ' ' + squareinb)

joinedstring = '\n'.join(possiblepairs) + '\n'
fileout.write(joinedstring)
fileout.close()
