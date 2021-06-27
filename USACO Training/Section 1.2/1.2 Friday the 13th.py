"""
ID: pranjal16
LANG: PYTHON3
TASK: friday
"""

filein = open('friday.in','r')
fileout = open('friday.out','w')

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
nOrCYear = [31,28,31,30,31,30,31,31,30,31,30,31]
leapYear = [31,29,31,30,31,30,31,31,30,31,30,31]
dayDict = {'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}

dayNumber = -1

N = int(filein.read().strip())

for year in range(1900,1900+N):
    if year%400 == 0:
        for month in leapYear:
            for i in range(month):
                dayNumber += 1
                if i == 12:
                    dayDict[days[dayNumber%7]] += 1
    elif year%100 == 0:
        for month in nOrCYear:
            for i in range(month):
                dayNumber += 1
                if i == 12:
                    dayDict[days[dayNumber%7]] += 1
    elif year%4 == 0:
        for month in leapYear:
            for i in range(month):
                dayNumber += 1
                if i == 12:
                    dayDict[days[dayNumber%7]] += 1
    else:
        for month in nOrCYear:
            for i in range(month):
                dayNumber += 1
                if i == 12:
                    dayDict[days[dayNumber%7]] += 1

fileout.write(str(dayDict['Saturday']) + ' ')
fileout.write(str(dayDict['Sunday']) + ' ')
fileout.write(str(dayDict['Monday']) + ' ')
fileout.write(str(dayDict['Tuesday']) + ' ')
fileout.write(str(dayDict['Wednesday']) + ' ')
fileout.write(str(dayDict['Thursday']) + ' ')
fileout.write(str(dayDict['Friday']) + '\n')
filein.close()
fileout.close()
