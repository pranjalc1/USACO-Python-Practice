filein = open('pails.in','r')
fileout = open('pails.out','w')

text = filein.readlines()
X,Y,M = [int(i) for i in text[0].split()]

filein.close()

# equation is X*x + Y*y <= M

maxx = M//X
answer = 0
for x in range(maxx+1):
    y = (M-X*x)//Y
    poss = X*x + Y*y
    if poss > answer:
        answer = poss

fileout.write(str(answer) + '\n')
fileout.close()
