filein = open('cowqueue.in','r')
fileout = open('cowqueue.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
times = [[int(i.split()[0]),int(i.split()[1])] for i in text]

filein.close()

times.sort(key = lambda x:x[0])

time = 0
for cow in times:
    if cow[0] > time:
        time = cow[0] + cow[1]
    else:
        time += cow[1]

fileout.write(str(time) + '\n')
fileout.close()
