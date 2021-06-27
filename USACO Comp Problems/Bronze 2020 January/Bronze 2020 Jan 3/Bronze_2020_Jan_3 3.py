filein = open('race.in.txt','r')
fileout = open('race.out.txt','w')

# read input
text = filein.readlines()
K,N = int(text[0].split()[0]),int(text[0].split()[1])
del text[0]

Xs = [int(text[i]) for i in range(N)]

filein.close()

# inspired by official solution
answers = {}
i = 1
dist = [0 for x in Xs]
numchanges = [0 for x in Xs]
notdone = True
while notdone:
    notdone = False
    for j in range(N):
        if K-dist[j] > 0:
            notdone = True
            dist[j] += i
            numchanges[j] += 1
            if K-dist[j] <= 0:
                answers[Xs[j]] = numchanges[j]
            if i >= Xs[j]:
                dist[j] += i
                numchanges[j] += 1
                if K-dist[j] <= 0:
                    answers[Xs[j]] = numchanges[j]
    i += 1

# output answers
answerstring = ''
for x in Xs:
    answerstring += str(answers[x]) + '\n'
fileout.write(answerstring)

fileout.close()
