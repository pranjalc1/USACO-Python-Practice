filein = open('billboard.in','r')
fileout = open('billboard.out','w')

text = filein.readlines()
ax1,ay1,ax2,ay2 = [int(i) for i in text[0].split()]
bx1,by1,bx2,by2 = [int(i) for i in text[1].split()]
cx1,cy1,cx2,cy2 = [int(i) for i in text[2].split()]

filein.close()

totalarea = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)

if (ax1 < cx1 < ax2 or ax2 > cx2 > ax1 or (cx1 < ax1 and cx2 > ax2)) and \
   (ay1 < cy1 < ay2 or ay2 > cy2 > ay1 or (cy1 < ay1 and cy2 > ay2)):
    boty = max(ay1,cy1)
    topy = min(ay2,cy2)
    botx = max(ax1,cx1)
    topx = min(ax2,cx2)
    possarea = (topy-boty)*(topx-botx)
    totalarea -= possarea

if (bx1 < cx1 < bx2 or bx2 > cx2 > bx1 or (cx1 < bx1 and cx2 > bx2)) and \
   (by1 < cy1 < by2 or by2 > cy2 > by1 or (cy1 < by1 and cy2 > by2)):
    boty = max(by1,cy1)
    topy = min(by2,cy2)
    botx = max(bx1,cx1)
    topx = min(bx2,cx2)
    possarea = (topy-boty)*(topx-botx)
    totalarea -= possarea

fileout.write(str(totalarea) + '\n')
fileout.close()
