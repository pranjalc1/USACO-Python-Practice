import sys

text = sys.stdin.readlines()
N = int(text.pop(0).strip())
cows = [int(i) for i in text[0].split()]
heights = [int(i) for i in text[1].split()]

possible = [[i] for i in range(N)]
for i in range(N-1):
    oldpossible = possible[:]
    possible = []
    for poss in oldpossible:
        for j in range(N):
            if j not in poss:
                possible.append(poss + [j])

answer = 0
for poss in possible:
    yes = True
    for cow in range(N):
        if cows[poss[cow]] > heights[cow]:
            yes = False
            break
    if yes:
        answer += 1

sys.stdout.write(str(answer) + '\n')
