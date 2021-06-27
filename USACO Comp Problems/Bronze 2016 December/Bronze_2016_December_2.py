filein = open('blocks.in','r')
fileout = open('blocks.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

words = []
for line in text:
    words.append(line.split())

filein.close()

letters = []
totalstring = ''
for block in words:
    totalstring += block[0] + block[1]

for letter in range(26):
    letters.append(totalstring.count(chr(letter+97)))

for letter in range(97,123):
    minsums = sum([min(block[0].count(chr(letter)),\
                       block[1].count(chr(letter))) for block in words])
    letters[letter-97] -= minsums

string = ''
for count in letters:
    string += str(count) + '\n'

fileout.write(string)
fileout.close()
