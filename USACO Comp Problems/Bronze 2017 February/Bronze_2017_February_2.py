filein = open('circlecross.in','r')
fileout = open('circlecross.out','w')

text = filein.readlines()
line = text[0].strip()

filein.close()

pairs = []
for i in range(65,90):
    for j in range(i+1,91):
        pairs.append([chr(i),chr(j)])

crossings = 0
for pair in pairs:
    a1,b1 = line.find(pair[0]),line.find(pair[1])
    a2,b2 = line.find(pair[0],a1+1),line.find(pair[1],b1+1)
    if a1 < b1 < a2 < b2 or b1 < a1 < b2 < a2:
        crossings += 1

fileout.write(str(crossings) + '\n')
fileout.close()
