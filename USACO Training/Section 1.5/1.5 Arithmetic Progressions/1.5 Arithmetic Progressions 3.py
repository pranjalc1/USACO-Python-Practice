"""
ID: pranjal16
LANG: PYTHON3
TASK: ariprog
"""

filein = open('ariprog.in','r')
fileout = open('ariprog.out','w')

text = filein.readlines()
N = int(text[0].strip())
M = int(text[1].strip())

filein.close()

isBisquare = [0 for i in range(2*M**2+1)]
for i in range(M+1):
    for j in range(i,M+1):
        isBisquare[i**2+j**2] = 1

S = []
for num in range(len(isBisquare)):
    if isBisquare[num]:
        S.append(num)

finalsols = []

for start in range(len(S)-N+1):
    maxb = (2*M**2 - start)//(N-1)
    for b in range(1,maxb+1):
        a = S[start]
        if a + b*(N-1) > 2*M**2:
            break
        check = True
        for i in range(1,N):
            if not isBisquare[a+i*b]:
                check = False
                break
        if check:
            finalsols.append([a,b])


finalsols.sort(key=lambda x:x[1])

if len(finalsols) == 0:
    fileout.write('NONE\n')
else:
    string = ''
    for finalsol in finalsols:
        string += str(finalsol[0]) + ' ' + str(finalsol[1]) + '\n'
    fileout.write(string)

fileout.close()
