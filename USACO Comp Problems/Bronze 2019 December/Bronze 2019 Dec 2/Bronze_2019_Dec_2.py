filein = open('whereami.in','r')
fileout = open('whereami.out','w')

lines = filein.readlines()

for i in range(2):
    lines[i] = lines[i].strip()

filein.close()

num = int(lines[0])
text = lines[1]
minimum = 100

for i in range(1,num+1):
    listofwords = []
    possible = []
    for j in range(0,num-i+1):
        listofwords += [text[j:j+i]]
    for a in range(num-i+1):
        for b in range(a+1,num-i+1):
            if listofwords[b] == listofwords[a]:
                possible.append(False)
            else:
                possible.append(True)
    if False not in possible and i < minimum:
        minimum = i

fileout.write(str(minimum) + '\n')
fileout.close()
