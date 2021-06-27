filein = open('shell.in','r')
fileout = open('shell.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

swaps = []
guesses = []
for i in range(N):
    text[i] = [int(x) for x in text[i].split()]
    swaps.append(text[i][:2])
    guesses.append(text[i][2])

filein.close()

first = 0
second = 0
third = 0

one = [1,0,0]
two = [0,1,0]
three = [0,0,1]

for swap in range(N):
    turn = swaps[swap]
    guess = guesses[swap]-1
    one[turn[0]-1],one[turn[1]-1] = one[turn[1]-1],one[turn[0]-1]
    two[turn[0]-1],two[turn[1]-1] = two[turn[1]-1],two[turn[0]-1]
    three[turn[0]-1],three[turn[1]-1] = three[turn[1]-1],three[turn[0]-1]
    if one[guess]:
        first += 1
    if two[guess]:
        second += 1
    if three[guess]:
        third += 1

fileout.write(str(max([first,second,third]))+'\n')
fileout.close()
