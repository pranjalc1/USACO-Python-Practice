"""
ID: pranjal16
LANG: PYTHON3
TASK: numtri
"""

filein = open('numtri.in','r')
fileout = open('numtri.out','w')

text = filein.readlines()
R = int(text.pop(0).strip())
rows = text[:]

for r in range(R):
    rows[r] = rows[r].split()
    for c in range(len(rows[r])):
        rows[r][c] = int(rows[r][c])

rows.reverse()

filein.close()

# solution inspired by Math Jam on aops.com

r = 0

while r < R-1:
    lasttworows = rows[:2]
    for c in range(len(lasttworows[1])):
        m = max(lasttworows[0][c],lasttworows[0][c+1])
        lasttworows[1][c] += m
    del lasttworows[0]
    if len(rows) == 2:
        rows = [lasttworows[0]]
    else:
        rows = lasttworows + rows[2:]
    r += 1

fileout.write(str(rows[0][0]) + '\n')
fileout.close()
