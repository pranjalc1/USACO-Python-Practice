filein = open('crossroad.in','r')
fileout = open('crossroad.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
obs = [[int(i.split()[0]),int(i.split()[1])] for i in text]

filein.close()

location = {}
for i in range(N):
    if obs[i][0] not in location.keys():
        location[obs[i][0]] = obs[i][1]

crossings = 0
for observe in range(N):
    if obs[observe][1] != location[obs[observe][0]]:
        location[obs[observe][0]] = obs[observe][1]
        crossings += 1

fileout.write(str(crossings) + '\n')
fileout.close()
