filein = open('loan.in','r')
fileout = open('loan.out','w')

text = filein.readlines()
N,K,M = text[0].split()
N,K,M = [int(i) for i in [N,K,M]]

filein.close()

# solution inspired by Carrara's solution
def find(possx):
    '''finds if possx is possible or not'''
    time = 0
    rem = N
    G = 0
    while rem > 0:
        G = (rem-G)//possx
        rem -= G
        time += 1
        if M*(K-time) >= rem:
            return True
        if G*(K-time) < rem:
            return False
    return time <= K

possX = 1
minX = 1
maxX = N
prevX = N
while True:
    if possX == prevX:
        answer = possX
        break
    prevX = possX
    possX = (minX+maxX)//2
    if find(possX):
        minX = possX
    else:
        maxX = possX

fileout.write(str(answer))
fileout.close()
