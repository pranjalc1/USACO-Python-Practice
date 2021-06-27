import sys

text = sys.stdin.readlines()
N = int(text.pop(0).strip())
cows = [int(i) for i in text[0].split()]
heights = [int(i) for i in text[1].split()]

possible = []
for cow in cows:
    possheights = []
    for height in range(N):
        if heights[height] >= cow:
            possheights.append(height)
    possible.append(possheights)

possible.sort(key = lambda i:len(i))
possible = [possible]
answer = 0

while len(possible) != 0 and len(possible[0]) != 0:
    oldpossible = possible[:]
    possible = []
    for poss in oldpossible:
        if poss == [poss[0] for i in range(len(poss))]:
            print(poss)
            newanswer = 1
            for i in range(1,len(poss) + 1):
                newanswer *= i
            answer += newanswer
        else:
            poss.sort(key = lambda i:len(i))
            for stall in poss[0]:
                newposs = [i.copy() for i in poss]
                del newposs[0]
                for cow in range(len(newposs)):
                    if stall in newposs[cow]:
                        index = newposs[cow].index(stall)
                        del newposs[cow][index]
                possible.append(newposs)
        possible.sort(key = lambda i:-len(i))

sys.stdout.write(str(answer) + '\n')
