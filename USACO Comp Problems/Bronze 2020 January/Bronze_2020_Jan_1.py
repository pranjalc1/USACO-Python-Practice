filein = open('word.in','r')
fileout = open('word.out','w')

# read filein
text = filein.readlines()
N,K = text[0].split()
N,K = int(N),int(K)
del text[0]

words = text[0].split()

filein.close()

# go through all the words
# add to the previous list in lines if new length <= K
lines = []
while len(words) != 0:
    if len(lines) == 0:
        lines.append([words[0]])
        del words[0]
    else:
        if len(words[0]) + len(''.join(lines[-1])) <= K:
            lines[-1].append(words[0])
        else:
            lines.append([words[0]])
        del words[0]

# change list items to strings
for i in range(len(lines)):
    lines[i] = ' '.join(lines[i])

# join the string and write solution
text = '\n'.join(lines) + '\n'
fileout.write(text)

fileout.close()
