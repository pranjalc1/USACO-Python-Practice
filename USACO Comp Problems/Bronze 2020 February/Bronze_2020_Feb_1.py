filein = open('triangles.in','r')
fileout = open('triangles.out','w')

# initialize values
points = filein.readlines()
N = int(points[0].strip())
del points[0]

for point in range(N):
    points[point] = points[point].split()
    points[point][0],points[point][1] = int(points[point][0]),\
                                        int(points[point][1])

filein.close()

# go through all possible pairings, find the area, and check if it is greater
# than the current max
maxarea2 = 0
for p1 in range(N-2):
    for p2 in range(p1+1,N-1):
        for p3 in range(p2+1,N):
            point1,point2,point3 = [points[x] for x in [p1,p2,p3]]
            xcoords = [point[0] for point in (point1,point2,point3)]
            ycoords = [point[1] for point in (point1,point2,point3)]
            if len(xcoords)-len(set(xcoords)) == 1 and \
               len(ycoords)-len(set(ycoords)) == 1:
                commonx = [xcoords[0]==xcoords[1],xcoords[0]==xcoords[2],\
                           xcoords[1]==xcoords[2]].index(True)
                commony = [ycoords[0]==ycoords[1],ycoords[0]==ycoords[2],\
                           ycoords[1]==ycoords[2]].index(True)
                vertical = [[point1,point2],[point1,point3],\
                            [point2,point3]][commonx]
                horizontal = [[point1,point2],[point1,point3],\
                              [point2,point3]][commony]
                if point1 in vertical and point1 in horizontal:
                    corner = point1
                if point2 in vertical and point2 in horizontal:
                    corner = point2
                if point3 in vertical and point3 in horizontal:
                    corner = point3
                vertical.remove(corner)
                horizontal.remove(corner)
                otherv = vertical[0]
                otherh = horizontal[0]
                x = abs(otherh[0]-corner[0])
                y = abs(otherv[1]-corner[1])
                area = x*y
                if area > maxarea2:
                    maxarea2 = area

# output answer
fileout.write(str(maxarea2) + '\n')
fileout.close()
