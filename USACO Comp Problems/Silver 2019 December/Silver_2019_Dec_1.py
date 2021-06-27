filein = open('moobuzz.in','r')
fileout = open('moobuzz.out','w')

N = int(filein.readlines()[0].strip())

filein.close()

possibilities = [14,1,2,4,7,8,11,13]
start = ((N-1)//8)*15
more = N % 8
num = start + possibilities[more]

fileout.write(str(num) + '\n')
fileout.close()
