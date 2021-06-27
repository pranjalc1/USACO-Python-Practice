filein = open('swap.in','r')
fileout = open('swap.out','w')

text = filein.readlines()
N,K = [int(i) for i in text.pop(0).split()]
a1,a2 = [int(i) for i in text.pop(0).split()]
b1,b2 = [int(i) for i in text[0].split()]

filein.close()

cows = list(range(1,N+1))
repeat = 0
prevnewcows = []
newcows = cows[:]
listofposs = [cows]
while True:
    prevnewcows = newcows[:]
    if a2 != len(newcows):
        newcows = prevnewcows[:a1-1] + list(reversed(prevnewcows[a1-1:a2])) + \
                  prevnewcows[a2:]
    else:
        newcows = prevnewcows[:a1-1] + list(reversed(prevnewcows[a1-1:]))
    if b2 != len(newcows):
        newcows = newcows[:b1-1] + list(reversed(newcows[b1-1:b2])) + \
                  newcows[b2:]
    else:
        newcows = newcows[:b1-1] + list(reversed(newcows[b1-1:]))
    repeat += 1
    if newcows == cows:
        check = 0
        break
    elif repeat == K:
        check = 1
        break
    listofposs.append(newcows)

if check:
    fileout.write('\n'.join([str(i) for i in newcows]) + '\n')
else:
    K = K%repeat
    fileout.write('\n'.join([str(i) for i in listofposs[K]]) + '\n')

fileout.close()
