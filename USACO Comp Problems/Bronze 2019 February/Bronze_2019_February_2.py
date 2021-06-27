filein = open('revegetate.in','r')
fileout = open('revegetate.out','w')

text = filein.readlines()
N,M = [int(i) for i in text.pop(0).split()]
for i in range(M):
    text[i] = [int(j) for j in text[i].split()]
    text[i].sort()
favorites = text[:]


filein.close()

possibilities = {i:[[j,i] for j in range(1,i)] for i in range(2,N+1)}

num = [1]
while len(num) < N:
    newlength = len(num) + 1
    poss = possibilities[newlength]
    find = []
    for comb in poss:
        if comb in favorites:
            find.append(num[comb[0]-1])
    find = list(set(find))
    possible = [1,2,3,4]
    for i in find:
        if i in possible:
            del possible[possible.index(i)]
    num.append(possible[0])

num.reverse()
answer = 0
for i in range(N):
    answer += num[i]*10**i

fileout.write(str(answer) + '\n')
