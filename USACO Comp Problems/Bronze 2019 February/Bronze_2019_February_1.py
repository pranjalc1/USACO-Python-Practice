filein = open('herding.in','r')
fileout = open('herding.out','w')

text = filein.readlines()
a,b,c = [int(i) for i in text[0].split()]
a,b,c = min(a,b,c),a+b+c-min(a,b,c)-max(a,b,c),max(a,b,c)

filein.close()

# first minimum
if b-a == 2 or c-b == 2:
    minimum = 1
else:
    minimum = 2

# then maximum
largestgap = max(c-b,b-a)
if largestgap == b-a:
    maximum = b-a-1
else:
    maximum = c-b-1

if b == a+1 and c == b+1:
    minimum = 0
    maximum = 0

fileout.write(str(minimum) + '\n' + str(maximum) + '\n')
fileout.close()
