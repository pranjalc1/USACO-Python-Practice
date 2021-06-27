filein = open('measurement.in','r')
fileout = open('measurement.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

measurements = []
for measure in text:
    measure = measure.split()
    measurements.append([int(measure[0])] + \
                        [['Bessie','Elsie','Mildred'].index(measure[1])] + \
                        [int(measure[2])])

filein.close()

measurements.sort(key = lambda m:m[0])
output = [7,7,7]
maxes = [0,1,2]
numchanges = 0

for measurement in measurements:
    prevmaxes = maxes[:]
    output[measurement[1]] += measurement[2]
    maxes = []
    for cow in range(3):
        if output[cow] == max(output):
            maxes.append(cow)
    if maxes != prevmaxes:
        numchanges += 1

fileout.write(str(numchanges) + '\n')
fileout.close()
