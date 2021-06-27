filein = open('photo.in','r')
fileout = open('photo.out','w')

# read filein
text = filein.readlines()
N = int(text[0].strip())
del text[0]

b = [int(i) for i in text[0].split()]

filein.close()

# finds sum of first and last terms
sumfirstlast = N*(N+1) - sum(b)

# check all possible sums and lists within the above sum
for first in range(1,sumfirstlast):
    last = sumfirstlast - first
    poss = [first]
    for term in b:
        if term-poss[-1] in poss or term-poss[-1] < 1:
            break
        else:
            poss.append(term-poss[-1])
    if len(poss) == N and len(set(poss)) == N and poss[-1] == last:
        a = poss[:]
        break

a = [str(i) for i in a]
answer = ' '.join(a) + '\n'
fileout.write(answer)

fileout.close()
