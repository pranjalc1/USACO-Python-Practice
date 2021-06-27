filein = open('teleport.in','r')
fileout = open('teleport.out','w')

text = filein.readlines()
text = [int(i) for i in text[0].split()]
startend = text[:2]
teleport = text[2:]

filein.close()

poss1 = abs(max(startend) - max(teleport)) + abs(min(startend) - min(teleport))
poss2 = max(startend) - min(startend)

fileout.write(str(min(poss1,poss2)) + '\n')
