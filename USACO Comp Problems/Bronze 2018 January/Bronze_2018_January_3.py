filein = open('outofplace.in','r')
fileout = open('outofplace.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

order = [int(line.strip()) for line in text]

filein.close()

numswaps = 0
correctorder = order[:]
correctorder.sort()
while order != correctorder:
    numswaps += 1
    for cow in range(N):
        if order[cow] != correctorder[cow]:
            break
    correctcow = correctorder[cow]
    where = order.index(correctcow)
    while order[where] == correctorder[where]:
        where = order.index(correctcow,where+1)
    wrongcow = order[cow]
    order[cow],order[where] = correctcow,wrongcow

fileout.write(str(numswaps) + '\n')
fileout.close()
