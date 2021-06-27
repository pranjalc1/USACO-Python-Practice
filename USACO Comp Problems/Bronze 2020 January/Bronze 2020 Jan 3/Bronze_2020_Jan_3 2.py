filein = open('race.in.txt','r')
fileout = open('race.out.txt','w')

# read input
text = filein.readlines()
K,N = int(text[0].split()[0]),int(text[0].split()[1])
del text[0]

Xs = [int(text[i]) for i in range(N)]

filein.close()

# approach takes TOO LONG and TOO MUCH MEMORY
# find all partitions of the distance
possible = [[1]]
while True:
    remaining = False
    oldpossible = possible[:]
    possible = []
    for poss in oldpossible:
        if poss[-1]:
            remaining = True
            lastterm = poss[-1]
            if poss[-1] != 1:
                last = [poss[-1]-i for i in range(1,-2,-1)]
            else:
                last = [poss[-1],poss[-1]+1]
            for posslast in last:
                newlist = poss + [posslast]
                if sum(newlist) >= K:
                    newlist.append(False)
                possible.append(newlist)
        else:
            possible.append(poss)
    if not remaining:
        break

# find answers
answers = {x:1000000000 for x in Xs}
for poss in possible:
    for x in Xs:
        if poss[-2] <= x and len(poss)-1 < answers[x]:
            answers[x] = len(poss)-1

# output answers
answerstring = ''
for x in Xs:
    answerstring += f'{answers[x]}\n'
fileout.write(answerstring)

fileout.close()
