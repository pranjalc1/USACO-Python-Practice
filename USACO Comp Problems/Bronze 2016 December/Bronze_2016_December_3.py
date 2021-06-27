filein = open('cowsignal.in','r')
fileout = open('cowsignal.out','w')

text = filein.readlines()
M,N,K = [int(i) for i in text[0].split()]
del text[0]

signal = [line.strip() for line in text]

filein.close()

intermsignal = []
for line in signal:
    string = ''
    for letter in line:
        string += letter*K
    intermsignal.append(string)

finalsignal = []
for line in intermsignal:
    for repeat in range(K):
        finalsignal.append(line)

fileout.write('\n'.join(finalsignal) + '\n')
fileout.close()
