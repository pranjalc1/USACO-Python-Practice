filein = open('breedflip.in','r')
fileout = open('breedflip.out','w')

text = filein.readlines()
N  = int(text.pop(0).strip())
A = list(text.pop(0).strip())
B = list(text[0].strip())

filein.close()

numchanges = 0
while B != A:
    firstd = 0
    for i in range(N):
        if A[i] != B[i]:
            firstd = i
            break
    lastd = 0
    for i in range(N-1,-1,-1):
        if A[i] != B[i]:
            lastd = i
            break
    for letter in range(firstd,lastd+1):
        if B[letter] == 'H':
            B[letter] = 'G'
        else:
            B[letter] = 'H'
    numchanges += 1

fileout.write(str(numchanges))
fileout.close()
