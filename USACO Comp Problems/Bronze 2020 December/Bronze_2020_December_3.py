import sys

text = sys.stdin.readlines()
N = int(text[0].strip())
del text[0]

positions = []
directions = []
dirconvert = {'N':[0,1],'E':[1,0]}
for line in text:
    info = line.split()
    directions.append(dirconvert[info[0]])
    positions.append([int(i) for i in info[1:]])

stopped = [positions[i] for i in range(N)]
intersections = []
times = []
losers = []

for cow1 in range(N-1):
    for cow2 in range(cow1,N):
        xa,ya,xb,yb = positions[cow1] + positions[cow2]
        dxa,dya,dxb,dyb = directions[cow1] + directions[cow2]
        possible = False
        if xa < xb and ya > yb:
            if dxa == 1 and dyb == 1:
                intersections.append([[xb,ya],[cow1,cow2]])
                possible = True
        elif xa > xb and ya < yb:
            if dxb == 1 and dya == 1:
                intersections.append([[xa,yb],[cow1,cow2]])
                possible = True
        if possible:
            xi,yi = [intersections[-1][0][i] for i in range(2)]
            times.append(xi-xa+yi-ya)
            times.append(xi-xb+yi-yb)
            if times[-2] > times[-1]:
                losers.append(0)
            elif times[-2] < times[-1]:
                losers.append(1)
            else:
                losers.append(2)

while len(intersections) > 0:
    mintime = min(times)
    when = times.index(mintime)
    where = when//2
    if losers[where] != 2:
        loser = [True,intersections[where][1][losers[where]]]
    else:
        loser = [False]
    if not loser[0]:
        del times[where*2:where*2+2]
        del intersections[where]
        del losers[where]
    else:
        stopped[loser[1]] = intersections[where][0]
        timestopped = times[where*2:where*2+2][losers[where]]
        cows = []
        for intersect in intersections:
            cows += intersect[1]
        numrepeats = 0
        intsbefore = []
        losersbefore = []
        timesbefore = []
        while loser[1] in cows:
            place = cows.index(loser[1])
            where = place//2
            if times[place] >= timestopped:
                del cows[where*2:where*2+2]
                del intersections[where]
                del losers[where]
                del times[where*2:where*2+2]
            else:
                timesbefore.append(times[where*2])
                timesbefore.append(times[where*2+1])
                losersbefore.append(losers[where])
                intsbefore.append(intersections[where])
                del cows[where*2:where*2+2]
                del intersections[where]
                del losers[where]
                del times[where*2:where*2+2]
        intersections += intsbefore
        losers += losersbefore
        times += timesbefore

distances = []
for cow in range(N):
    xs,ys = stopped[cow]
    xc,yc = positions[cow]
    distances.append(xs-xc+ys-yc)
    if distances[-1] == 0:
        distances[-1] = 'Infinity'
    distances[-1] = str(distances[-1])

sys.stdout.write('\n'.join(distances) + '\n')
