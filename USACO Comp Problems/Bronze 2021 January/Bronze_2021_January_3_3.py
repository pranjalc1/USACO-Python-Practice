import sys

text = sys.stdin.readlines()
N = int(text.pop(0).strip())
cows = [int(i) for i in text[0].split()]
heights = [int(i) for i in text[1].split()]

possible = [[i] for i in range(N) if cows[i] <= heights[0]]

while len(possible[0]) != N and len(possible) != 0:
    oldpossible = possible[:]
    possible = []
    for poss in oldpossible:
        newpossibles = [poss + [i] for i in range(N) \
                        if cows[i] <= heights[len(poss)] and \
                        i not in poss]
        possible += newpossibles

answer = len(possible)

sys.stdout.write(str(answer) + '\n')
