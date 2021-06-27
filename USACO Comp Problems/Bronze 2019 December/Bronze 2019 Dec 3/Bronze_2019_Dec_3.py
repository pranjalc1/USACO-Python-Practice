filein = open('lineup.in','r')
fileout = open('lineup.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

constraints = []
for line in range(N):
    constraints.append(text[line].split()[0:6:5])

filein.close()

# make list of names, sort, and convert to numbers
names = ['Bessie','Buttercup','Belinda','Beatrice',\
         'Bella','Blue','Betsy','Sue']
names.sort()

namenum = {}
numname = {}
for i in range(8):
    namenum[names[i]] = i+1
    numname[i+1] = names[i]
nums = list(range(1,9))

# change constraints to numbers
for constraint in constraints:
    constraint[0] = namenum[constraint[0]]
    constraint[1] = namenum[constraint[1]]

# find all possible combinations and see which ones are possible
posscombos = []
i = 0
while i < 8:
    oldcombos = posscombos[:]
    posscombos = []
    if i == 0:
        posscombos = ['1','2','3','4','5','6','7','8']
    else:
        for combo in oldcombos:
            for j in range(1,9):
                if str(j) not in combo:
                    posscombos.append(combo + str(j))
    i += 1

# earlier I was finding all of the solutions, but it is easier to find the first one
# this is inspired by Brian Dean's first solution on USACO
posscombos.sort()
for combo in posscombos:
    check = True
    for constraint in constraints:
        if abs(combo.index(str(constraint[0])) \
        - combo.index(str(constraint[1]))) - 1:
            check = False
            break
    if check:
        finalstring = ''
        for num in combo:
            finalstring += numname[int(num)] + '\n'
        fileout.write(finalstring)
        fileout.close()
        break
