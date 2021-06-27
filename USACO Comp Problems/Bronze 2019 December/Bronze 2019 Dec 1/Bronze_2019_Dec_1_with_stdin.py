import sys

text = sys.stdin.readlines()
for i in range(len(text)):
    text[i] = text[i].split()

k = int(text[0][0])
n = int(text[0][1])
rounds = text[1:]
for i in range(len(rounds)):
    for j in range(len(rounds[i])):
        rounds[i][j] = int(rounds[i][j])

pairs = {}
for i in range(n):
    for j in range(i+1,n):
        pairs[(rounds[0][i],rounds[0][j])] = 0

for aRound in rounds:
    for pair in pairs:
        if aRound.index(pair[0]) < aRound.index(pair[1]):
            pairs[pair] += 1

total = 0
for pair in pairs:
    if pairs[pair] == k:
        total += 1

sys.stdout.write(str(total) + '\n')
