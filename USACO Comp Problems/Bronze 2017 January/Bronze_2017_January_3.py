filein = open('cowtip.in','r')
fileout = open('cowtip.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
grid = [[int(i) for i in line.strip()] for line in text]

filein.close()

numflips = 0
while True:
    sumoflists = sum([sum(line) for line in grid])
    if sumoflists == 0:
        break
    for i in range(N-1,-1,-1):
        if sum(grid[i]) > 0:
            maxdown = i
            break
    for j in range(N-1,-1,-1):
        if grid[maxdown][j] == 1:
            maxright = j
            break
    for x in range(maxright+1):
        for y in range(maxdown+1):
            grid[y][x] = 1 - grid[y][x]
    numflips += 1

fileout.write(str(numflips) + '\n')
fileout.close()
