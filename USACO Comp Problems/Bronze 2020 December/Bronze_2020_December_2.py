import sys

text = sys.stdin.readlines()
N = int(text[0].strip())
del text[0]

petals = [int(i) for i in text[0].split()]

def average(i,j):
    '''finds the average of the petals from i to j
    and checks if there is an average flower'''
    avg = sum(petals[i:j+1])/(j-i+1)
    return avg in petals[i:j+1]

total = 0
for i in range(N):
    for j in range(i,N):
        if average(i,j):
            total += 1

sys.stdout.write(str(total) + '\n')
