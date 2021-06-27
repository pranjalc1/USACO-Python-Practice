filein = open('socdist1.in','r')
fileout = open('socdist1.out','w')

# scan input
text = filein.readlines()
N = int(text[0].strip())
del text[0]

# make list of stalls and breaks
text = text[0].strip()
stalls = []
num1s = 0
for i in range(N):
    if int(text[i]):
        stalls.append(1)
        num1s += 1
    else:
        stalls.append(0)

filein.close()

breaks = text.split('1')
lenbreaks = []
for i in range(len(breaks)):
    breaks[i] = [int(j) for j in breaks[i]]
while [] in breaks:
    breaks.remove([])
lenbreaks = [len(i)+1 for i in breaks]

# find the leading and trailing zeroes
beg = 0
end = 0
middle = False
if len(lenbreaks) > 2:
    middle = True
if text[0] == '0':
    beg = lenbreaks.pop(0)-1
if text[-1] == '0' and len(lenbreaks) != 0:
    end = lenbreaks.pop(-1)-1

# find the maximum d and the second max
if len(lenbreaks) != 0:
    maxD = max(lenbreaks)
    lenbreaks.remove(maxD)
    if len(lenbreaks) != 0:
        smaxD = max(lenbreaks)
    else:
        smaxD = 0
    lenbreaks.append(maxD)
else:
    maxD = 0

# both cows if no beginning or end
if not beg and not end:
    if maxD//3 >= smaxD//2:
        lenbreaks.remove(maxD)
        if not maxD % 3:
            for i in range(3):
                lenbreaks.append(maxD//3)
        elif maxD % 3 == 1:
            lenbreaks.append(maxD//3)
            lenbreaks.append(maxD//3)
            lenbreaks.append(maxD//3 + 1)
        else:
            for i in range(2):
                lenbreaks.append(maxD//3 + 1)
            lenbreaks.append(maxD//3)
    else:
        lenbreaks.remove(maxD)
        lenbreaks.remove(smaxD)
        if not maxD % 2:
            for i in range(2):
                lenbreaks.append(maxD//2)
        else:
            for i in range(2):
                lenbreaks.append(maxD//2+i)
        if not smaxD % 2:
            for i in range(2):
                lenbreaks.append(smaxD//2)
        else:
            for i in range(2):
                lenbreaks.append(smaxD//2+i)
else:
    # first cow
    if beg >= maxD//2 and beg >= end:
        lenbreaks.append(beg)
        beg = 0
    elif end >= maxD//2 and end >= beg:
        lenbreaks.append(end)
        end = 0
    elif maxD//2 >= beg and maxD//2 >= end:
        lenbreaks.remove(maxD)
        for i in range(2):
            lenbreaks.append(maxD//2+i)
    # new max
    maxD = max(lenbreaks)
    
    # second cow
    if beg >= maxD//2 and beg >= end:
        lenbreaks.append(beg)
        beg = 0
    elif end >= maxD//2 and end >= beg:
        lenbreaks.append(end)
        end = 0
    elif maxD//2 >= beg and maxD//2 >= end:
        lenbreaks.remove(maxD)
        for i in range(2):
            lenbreaks.append(maxD//2+i)

# output (only case where the above program does not work is when there are only
# 0s, so include this possibility
minimum = min(lenbreaks)
if minimum == 0:
    minimum += 1
if not num1s:
    minimum = len(text)-1
fileout.write(str(minimum)+'\n')
fileout.close()
