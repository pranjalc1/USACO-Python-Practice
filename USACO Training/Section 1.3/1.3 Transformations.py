'''
ID: pranjal16
LANG: PYTHON3
TASK: transform
'''

filein = open('transform.in','r')
fileout = open('transform.out','w')

text = filein.readlines()
for line in range(len(text)):
    text[line] = text[line].strip()

N = int(text[0])
list1 = text[1:N+1]
list2 = text[N+1:]

filein.close()

for row in range(N):
    list1[row] = list(list1[row])
    list2[row] = list(list2[row])

def f1(inlist):
    '''90 degrees clockwise'''
    newlist = []
    x = len(inlist)
    for row in range(x):
        newlist.append([inlist[r][row] for r in range(x-1,-1,-1)])
    return newlist

def f2(inlist):
    '''180 degrees clockwise'''
    return f1(f1(inlist))

def f3(inlist):
    '''270 degrees clockwise'''
    return f1(f1(f1(inlist)))

def f4(inlist):
    '''reflection about vertical axis'''
    return [row[::-1] for row in inlist]

if f1(list1) == list2:
    fileout.write('1\n')
elif f2(list1) == list2:
    fileout.write('2\n')
elif f3(list1) == list2:
    fileout.write('3\n')
elif f4(list1) == list2:
    fileout.write('4\n')
elif f1(f4(list1)) == list2:
    fileout.write('5\n')
elif f2(f4(list1)) == list2:
    fileout.write('5\n')
elif f3(f4(list1)) == list2:
    fileout.write('5\n')
elif list1 == list2:
    fileout.write('6\n')
else:
    fileout.write('7\n')

fileout.close()
