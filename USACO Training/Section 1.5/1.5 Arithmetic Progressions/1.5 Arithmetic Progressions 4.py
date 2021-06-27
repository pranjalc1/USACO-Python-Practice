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

S = []
for i in range(M+1):
    for j in range(i,M+1):
        if i**2+j**2 not in S:
            S.append(i**2+j**2)

S.sort()

finalsols = []
for start in range(len(S)):
    for second in range(start+1,len(S)):
        one = S[start]
        two = S[second]
        change = two-one
        if start + change*(N-1) <= 2*M**2:
            finalsols.append([one,change])
            aTry = True
            newelement = two
            for i in range(N-2):
                newelement += change
                if newelement not in S:
                    aTry = False
                    break
            if not aTry:
                del finalsols[-1]

finalsols.sort(key=lambda x:x[0])
finalsols.sort(key=lambda x:x[1])

if len(finalsols) == 0:
    fileout.write('NONE\n')
else:
    string = ''
    for finalsol in finalsols:
        string += str(finalsol[0]) + ' ' + str(finalsol[1]) + '\n'
    fileout.write(string)

fileout.close()
