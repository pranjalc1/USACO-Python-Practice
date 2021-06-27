filein = open('taming.in','r')
fileout = open('taming.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
log = [int(i) for i in text[0].split()]

filein.close()

if log[0] == -1:
    log[0] = 0

def check(log):
    '''check the log if it works'''
    for measure in range(N):
        if log[measure] == 0 or log[measure] == -1 or \
           (measure > 0 and log[measure] - log[measure-1] == 1):
            continue
        else:
            return False
    if log[0] != 0:
        return False
    return True

for entry in range(N):
    if log[entry] > 0:
        for i in range(entry-1,-1,-1):
            if log[i] == -1:
                newentry = log[entry] - entry + i
                if newentry == -1:
                    break
                log[i] = newentry
            else:
                break

checklog = check(log)
if not checklog:
    fileout.write(str(-1) + '\n')
else:
    count = log.count(0)
    possmore = log.count(-1)
    fileout.write(str(count) + ' ' + str(count+possmore) + '\n')

fileout.close()
