filein = open('traffic.in','r')
fileout = open('traffic.out','w')

text = filein.readlines()
N = int(text.pop(0))

miles = []
for mile in text:
    mile = mile.split()
    miles.append([mile[0],int(mile[1]),int(mile[2])])

filein.close()

# finding the minimum cars before the first mile
mile = 0
ons = []
offs = []
minb = 0
while mile < N:
    seg = miles[mile]
    if seg[0] == 'on':
        ons.append(seg[2])
    elif seg[0] == 'off':
        offs.append(seg[1])
    else:
        possible = seg[1] - sum(ons) + sum(offs)
        if possible > minb:
            minb = possible
    mile += 1

# finding the maximum cars before the first mile
mile = 0
ons = []
offs = []
maxb = 10**9
while mile < N:
    seg = miles[mile]
    if seg[0] == 'on':
        ons.append(seg[1])
    elif seg[0] == 'off':
        offs.append(seg[2])
    else:
        possible = seg[2] - sum(ons) + sum(offs)
        if possible < maxb:
            maxb = possible
    mile += 1

miles.reverse()
for mile in range(N):
    if miles[mile][0] == 'on':
        miles[mile][0] = 'off'
    elif miles[mile][0] == 'off':
        miles[mile][0] = 'on'

# finding the minimum cars after the last mile
mile = 0
ons = []
offs = []
mina = 0
while mile < N:
    seg = miles[mile]
    if seg[0] == 'on':
        ons.append(seg[2])
    elif seg[0] == 'off':
        offs.append(seg[1])
    else:
        possible = seg[1] - sum(ons) + sum(offs)
        if possible > mina:
            mina = possible
    mile += 1

# finding the maximum cars after the last mile
mile = 0
ons = []
offs = []
maxa = 10**9
while mile < N:
    seg = miles[mile]
    if seg[0] == 'on':
        ons.append(seg[1])
    elif seg[0] == 'off':
        offs.append(seg[2])
    else:
        possible = seg[2] - sum(ons) + sum(offs)
        if possible < maxa:
            maxa = possible
    mile += 1

fileout.write(str(minb) + ' ' + str(maxb) + '\n' + \
              str(mina) + ' ' + str(maxa) + '\n')
fileout.close()
