'''
ID: pranjal16
LANG: PYTHON3
TASK: milk
'''

filein = open('milk.in','r')
fileout = open('milk.out','w')

text = filein.readlines()
splittext = [line.split() for line in text]

for line in range(len(splittext)):
    for i in range(2):
        splittext[line][i] = int(splittext[line][i])

N = splittext[0][0]
M = splittext[0][1]

del splittext[0]

filein.close()

splittext.sort(key = lambda x:x[0])

totalunits = 0
totalcost = 0

while totalunits < N:
    unitsfromfarmer = splittext[0][1]
    if unitsfromfarmer >= N - totalunits:
        totalcost += (N - totalunits) * splittext[0][0]
        totalunits = N
    else:
        totalunits += unitsfromfarmer
        totalcost += unitsfromfarmer * splittext[0][0]
        del splittext[0]

fileout.write(str(totalcost) + '\n')
fileout.close()
