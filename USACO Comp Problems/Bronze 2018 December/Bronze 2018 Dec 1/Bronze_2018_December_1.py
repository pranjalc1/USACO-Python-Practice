filein = open('mixmilk.in','r')
fileout = open('mixmilk.out','w')

# scan input
text = filein.readlines()
b1 = [int(i) for i in text[0].split()]
b2 = [int(i) for i in text[1].split()]
b3 = [int(i) for i in text[2].split()]

filein.close()

# pour from first bucket to second bucket
def pour(first,second):
    '''pours from one bucket to the next'''
    c1 = first[0]
    i1 = first[1]
    c2 = second[0]
    i2 = second[1]
    if i1 <= c2 - i2:
        return ([c1,0],[c2,i1+i2])
    else:
        return ([c1,i1-(c2-i2)],[c2,c2])

# do all of the 100 pours
for move in range(100):
    if move % 3 == 0:
        b1,b2 = pour(b1,b2)
    elif move % 3 == 1:
        b2,b3 = pour(b2,b3)
    else:
        b3,b1 = pour(b3,b1)

# output answer
string = ''
for bucket in [b1,b2,b3]:
    string += str(bucket[1]) + '\n'

fileout.write(string)
fileout.close()
