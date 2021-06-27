filein = open('notlast.in','r')
fileout = open('notlast.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
cows = {i:0 for i in ['Bessie', 'Elsie', 'Daisy', 'Gertie', \
                      'Annabelle', 'Maggie', 'Henrietta']}
for cow in text:
    name,num = cow.split()[0],int(cow.split()[1])
    cows[name] += num

filein.close()

cowlist = [[i,cows[i]] for i in cows]
minimum = min([i[1] for i in cowlist])

while minimum in [cow[1] for cow in cowlist]:
    for cow in cowlist:
        if cow[1] == minimum:
            cowlist.remove(cow)
if len(cowlist) == 0:
    fileout.write('Tie\n')
else:
    cowlist.sort(key = lambda x:x[1])
    smin = cowlist[0][1]
    if [i[1] for i in cowlist].count(smin) > 1:
        fileout.write('Tie\n')
    else:
        fileout.write(cowlist[0][0] + '\n')

fileout.close()
