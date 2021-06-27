filein = open('race.in','r')
fileout = open('race.out','w')

# read input
text = filein.readlines()
K,N = int(text[0].split()[0]),int(text[0].split()[1])
del text[0]

Xs = [int(text[i]) for i in range(N)]

filein.close()

# inspired by solution by HJKZ
def answer(possx):
    '''finds answer with a maximum ending speed of x with binary search'''
    tmin = K+1
    maxs = K+1
    mins = 0
    lasts = 0
    while mins <= maxs:
        s = (mins+maxs)//2
        if s == lasts:
            return tmin
        lasts = s
        
        acc = s*(s+1)//2
        dec = acc - possx*(possx-1)//2
        if possx >= s:
            dec = 0
        
        tot = acc + dec
        final = min(possx,s)
        if tot - final >= K:
            maxs = s
            continue
        
        hor = (K-tot)//s*s
        time = s + s-possx+1 + hor//s
        
        if dec == 0:
            time -= s-possx+1
        if tot + hor < K:
            time += 1
        
        tmin = min(time,tmin)
        mins = s
    return tmin
        

# output answers
answerstring = ''
for x in Xs:
    answerstring += str(answer(x)) + '\n'
fileout.write(answerstring)

fileout.close()
