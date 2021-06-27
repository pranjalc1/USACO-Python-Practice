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

# int list, where if the index is a bisquare it is 1
isBisquare = [0 for i in range(2*M**2+1)]
for i in range(M+1):
    for j in range(i,M+1):
        isBisquare[i**2+j**2] = 1

# finds the bisquares (ordered)
S = []
for num in range(len(isBisquare)):
    if isBisquare[num]:
        S.append(num)

# search and sort
finalsols = []
for start in range(len(S)-N+1):
    # designate start
    one = S[start]
    for second in range(start+1,len(S)-N+2):
        # designate second term
        two = S[second]
        change = two - one
        
        # largest term has to be small enough
        if one + (N-1)*change > 2*M**2:
            break
        
        # goes through all terms to find if any is not in the sequence
        check = True
        for term in range(two+change,one+change*N,change):
            if not isBisquare[term]:
                check = False
                break
        
        # if the sequence is correct then add it to solutions
        if check:
            finalsols.append([one,change])

finalsols.sort(key=lambda x:x[1])

# output solution
if len(finalsols) == 0:
    fileout.write('NONE\n')
else:
    string = ''
    for finalsol in finalsols:
        string += str(finalsol[0]) + ' ' + str(finalsol[1]) + '\n'
    fileout.write(string)

fileout.close()
