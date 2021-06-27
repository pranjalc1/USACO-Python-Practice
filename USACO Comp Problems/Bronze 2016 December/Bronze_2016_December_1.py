filein = open('square.in','r')
fileout = open('square.out','w')

text = filein.readlines()
ax1,ay1,ax2,ay2 = [int(i) for i in text[0].split()]
bx1,by1,bx2,by2 = [int(i) for i in text[1].split()]

filein.close()

horiz = max(ax2,bx2) - min(ax1,bx1)
vert = max(ay2,by2) - min(ay1,by1)
maxside = max(horiz,vert)

area = maxside**2
fileout.write(str(area) + '\n')
fileout.close()
