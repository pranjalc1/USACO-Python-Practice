filein = open('blist.in','r')
fileout = open('blist.out','w')

# scan input
text = filein.readlines()
N = int(text[0].strip())
del text[0]

starts = []
ends = []
buckets = []

for line in text:
    newline = line.split()
    starts.append(int(newline[0]))
    ends.append(int(newline[1]))
    buckets.append(int(newline[2]))

totaltime = max(ends)

filein.close()

# go through all of the times, adding buckets as necessary
totalbuckets = 0
for time in range(1,totaltime+1):
    if time in starts:
        cow = starts.index(time)
        bcow = buckets[cow]
        if bcow > totalbuckets:
            totalbuckets = 0
        else:
            totalbuckets -= bcow
    elif time in ends:
        cow = ends.index(time)
        bcow = buckets[cow]
        totalbuckets += bcow

# output answer
fileout.write(str(totalbuckets)+'\n')
fileout.close()
