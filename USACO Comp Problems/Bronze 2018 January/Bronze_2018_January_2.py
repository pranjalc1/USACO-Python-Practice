filein = open('lifeguards.in','r')
fileout = open('lifeguards.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

guards = [[int(text[i].split()[0]),int(text[i].split()[1])] \
              for i in range(N)]

for i in range(N):
    guards[i] = list(range(guards[i][0]+1,guards[i][1]+1))

filein.close()

maxtime = 0
for guard in guards:
    possguards = guards[:]
    possguards.remove(guard)
    total = []
    for i in possguards:
        total += i
    total = set(total)
    posstime = len(total)
    if posstime > maxtime:
        maxtime = posstime

fileout.write(str(maxtime) + '\n')
fileout.close()
