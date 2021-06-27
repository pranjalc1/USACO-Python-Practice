filein = open('guess.in','r')
fileout = open('guess.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
text = [line.split() for line in text]
animals = [text[num][0] for num in range(N)]
character = {animals[num]:text[num][2:] for num in range(N)}

filein.close()

pairs = []
for animal in range(N-1):
    for second in range(animal+1,N):
        combined = character[animals[animal]] + character[animals[second]]
        pairs.append(len(combined)-len(set(combined)))

answer = max(pairs) + 1
fileout.write(str(answer) + '\n')
fileout.close()
