'''
ID: pranjal16
LANG: PYTHON3
TASK: combo
'''

filein = open('combo.in','r')
fileout = open('combo.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

numbers = []
numbers.append(text[0].split())
numbers.append(text[1].split())
for n in range(3):
    numbers[0][n] = int(numbers[0][n])
    numbers[1][n] = int(numbers[1][n])

filein.close()

possiblesolutions = []
for i in range(numbers[0][0]-2,numbers[0][0]+3):
    for j in range(numbers[0][1]-2,numbers[0][1]+3):
        for k in range(numbers[0][2]-2,numbers[0][2]+3):
            if [i%N,j%N,k%N] not in possiblesolutions:
                possiblesolutions.append([i%N,j%N,k%N])
            

for i in range(numbers[1][0]-2,numbers[1][0]+3):
    for j in range(numbers[1][1]-2,numbers[1][1]+3):
        for k in range(numbers[1][2]-2,numbers[1][2]+3):
            if [i%N,j%N,k%N] not in possiblesolutions:
                possiblesolutions.append([i%N,j%N,k%N])

numsolutions = len(possiblesolutions)

fileout.write(str(numsolutions) + '\n')
fileout.close()
