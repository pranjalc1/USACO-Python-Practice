filein = open('race.in.txt','r')
fileout = open('race.out.txt','w')

# read input
text = filein.readlines()
K,N = int(text[0].split()[0]),int(text[0].split()[1])
del text[0]

Xs = [int(text[i]) for i in range(N)]

filein.close()

# inspired by solution by Carrara
def answer(x):
    '''finds answer with a maximum ending speed of x'''
    y = 0
    while (y+1)*(y+2)//2 <= K:
        y += 1
    if y*(y+1)//2 == K and y <= x:
        return y
    elif K-y*(y+1)//2 <= y and y <= x:
        return y+1
    elif K-y*(y+1) <= 2*y and y <= x:
        return y+2
    y = 0
    r = x*(x-1)//2 + K
    while (y+1)**2 <= r:
        y += 1
    if y**2 == r:
        return 2*y-x
    elif r - y**2 <= y:
        return 2*y-x+1
    elif r - y**2 <= 2*y:
        return 2*y-x+2

# output answers
answerstring = ''
for x in Xs:
    answerstring += str(answer(x)) + '\n'
fileout.write(answerstring)

fileout.close()
