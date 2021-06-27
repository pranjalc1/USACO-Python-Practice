filein = open('shuffle.in','r')
fileout = open('shuffle.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

text[0] = [int(i) for i in text[0].split()]
revshuffle = {}
for i in range(1,N+1):
    revshuffle[text[0].index(i)+1] = i
del text[0]
print(revshuffle)
IDs = [int(i) for i in text[0].split()]
positions = list(range(1,N+1))

filein.close()

for shuffle in range(3):
    for cow in range(N):
        positions[cow] = revshuffle[positions[cow]]

answer = ''
for cow in range(N):
    answer += str(IDs[positions[cow]-1]) + '\n'

fileout.write(answer)
fileout.close()
