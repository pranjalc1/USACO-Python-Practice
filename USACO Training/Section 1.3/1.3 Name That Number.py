'''
ID: pranjal16
LANG: PYTHON3
TASK: namenum
'''

dictionary = open('dict.txt','r')
filein = open('namenum.in','r')
fileout = open('namenum.out','w')

names = dictionary.readlines()
for line in range(len(names)):
    names[line] = names[line].strip()

dictionary.close()

N = filein.readlines()[0].strip()

filein.close()

lettertonum = {}
for letter in ['A','B','C']:
    lettertonum[letter] = '2'
for letter in ['J','K','L']:
    lettertonum[letter] = '5'
for letter in ['T','U','V']:
    lettertonum[letter] = '8'
for letter in ['D','E','F']:
    lettertonum[letter] = '3'
for letter in ['M','N','O']:
    lettertonum[letter] = '6'
for letter in ['W','X','Y']:
    lettertonum[letter] = '9'
for letter in ['G','H','I']:
    lettertonum[letter] = '4'
for letter in ['P','R','S']:
    lettertonum[letter] = '7'

realnames = []
for name in names:
    canbe = True
    num = ''
    for letter in name:
        if letter in lettertonum:
            num += lettertonum[letter]
        else:
            canbe = False
    if canbe and num == N:
        realnames.append(name)
        

if len(realnames) == 0:
    fileout.write('NONE\n')
else:
    fileout.write('\n'.join(realnames) + '\n')

fileout.close()
