"""
ID: pranjal16
LANG: PYTHON3
TASK: beads
"""

filein = open('beads.in','r')
text = filein.readlines()
filein.close()

for line in range(len(text)):
    text[line] = text[line].strip()

num = int(text[0])
newtext = ''
maxim = 0

for i in range(num):
    newtext = (text[1][i:num] + text[1][0:i])*2
    count1 = 0
    count2 = 0
    j = num
    k = num-1
    while j < 2*num and newtext[j] == 'w':
        count1 += 1
        j += 1
    while k >= 0 and newtext[k] == 'w':
        count2 += 1
        k -= 1
    if j != 2*num:
        l1 = newtext[j]
    else:
        l1 = 'w'
    if k != -1:
        l2 = newtext[k]
    else:
        l2 = 'w'
    if l1 != 'w' and l2 != 'w':
        while j < 2*num and (newtext[j] == 'w' or newtext[j] == l1):
            count1 += 1
            j += 1
        while k >= 0 and (newtext[k] == 'w' or newtext[k] == l2):
            count2 += 1
            k -= 1
    elif l1 == 'w' and l2 !='w':
        while k >= 0 and (newtext[k] == 'w' or newtext[k] == l2):
            count2 += 1
            k -= 1
    elif l2 == 'w' and l1 != 'w':
        while j < 2*num and (newtext[j] == 'w' or newtext[j] == l1):
            count1 += 1
            j += 1
    if count1 + count2 > maxim:
        maxim = count1 + count2

if maxim > num:
    maxim = num

fileout = open('beads.out','w')
fileout.write(str(maxim)+'\n')
fileout.close()
