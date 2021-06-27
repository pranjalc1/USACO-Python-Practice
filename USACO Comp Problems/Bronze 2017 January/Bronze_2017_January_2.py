filein = open('hps.in','r')
fileout = open('hps.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
rounds = []
for game in text:
    rounds.append([int(i) for i in game.split()])

filein.close()

poss1 = 0
poss2 = 0

for game in rounds:
    if game in [[1,2],[2,3],[3,1]]:
        poss1 += 1
    elif game in [[1,3],[3,2],[2,1]]:
        poss2 += 1

fileout.write(str(max([poss1,poss2])) + '\n')
fileout.close()
