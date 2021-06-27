filein = open('backforth.in','r')
fileout = open('backforth.out','w')

# scan input
text = filein.readlines()
storage1 = [int(i) for i in text[0].split()] + [1000]
storage2 = [int(i) for i in text[1].split()] + [1000]
filein.close()

# use recursion to go through all possible combinations
# output all of the possiibilities
possible = []
def find(bucket1,bucket2,time):
    '''finds all possible amounts of milk in tank'''
    if time == 0 or time == 2:
        for bucket in bucket1[:-1]:
            newbucket1 = bucket1[:-1]
            newbucket1.remove(bucket)
            newbucket1.append(bucket1[-1] - bucket)
            newbucket2 = bucket2[:-1]
            newbucket2.append(bucket)
            newbucket2.append(bucket2[-1] + bucket)
            find(newbucket1,newbucket2,time+1)
    elif time == 1 or time == 3:
        for bucket in bucket2[:-1]:
            newbucket2 = bucket2[:-1]
            newbucket2.remove(bucket)
            newbucket2.append(bucket2[-1] - bucket)
            newbucket1 = bucket1[:-1]
            newbucket1.append(bucket)
            newbucket1.append(bucket1[-1] + bucket)
            find(newbucket1,newbucket2,time+1)
    else:
        possible.append(bucket1[-1])

# find possibilities
find(storage1,storage2,0)
possible = list(set(possible))

# output answers
fileout.write(str(len(possible)) + '\n')

fileout.close()
