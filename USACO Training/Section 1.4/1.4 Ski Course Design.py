'''
ID: pranjal16
LANG: PYTHON3
TASK: skidesign
'''

filein = open('skidesign.in','r')
fileout = open('skidesign.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

for i in range(N):
    text[i] = int(text[i].strip())

filein.close()

numbers = text[:]

# Inspired by hint from Fatih Gelgi's solution
# that is on http://www.usaco.org/current/data/sol_skidesign.html
minmoney = 10**1000
for low in range(84):
    high = low + 17
    cost = 0
    for num in numbers:
        if num < low:
            cost += (num - low)**2
        elif num > high:
            cost += (num - high)**2
    if cost <= minmoney:
        minmoney = cost

fileout.write(str(minmoney) + '\n')
fileout.close()
