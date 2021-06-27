"""
ID: pranjal16
LANG: PYTHON3
TASK: milk2
"""

filein = open('milk2.in','r' )
fileout = open('milk2.out','w')

text = filein.readlines()

N = int(text[0].strip())
times = []

for line in range(1,N+1):
    times.append(text[line].split())

filein.close()

for time in range(N):
    for n in range(2):
        times[time][n] = int(times[time][n])

times.sort()

time = 0
milkings = []

while time < N:
    if time == 0:
        milkings.append(times[time])
    elif times[time][0] <= milkings[-1][1] and times[time][1] >= milkings[-1][1]:
        milkings[-1][1] = times[time][1]
    elif times[time][0] > milkings[-1][1]:
        milkings.append(times[time])
    time += 1

longestMilk = 0

for milk in milkings:
    if milk[1] - milk[0] > longestMilk:
        longestMilk = milk[1] - milk[0]

longestGap = 0

for time in range(1,len(milkings)):
    if milkings[time][0] - milkings[time-1][1] > longestGap:
        longestGap = milkings[time][0] - milkings[time-1][1]


fileout.write(f'{longestMilk} {longestGap}\n')
fileout.close()
