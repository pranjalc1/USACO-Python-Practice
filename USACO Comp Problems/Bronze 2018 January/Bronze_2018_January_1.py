filein = open('billboard.in','r')
fileout = open('billboard.out','w')

text = filein.readlines()
ax1,ay1,ax2,ay2 = [int(i) for i in text[0].split()]
bx1,by1,bx2,by2 = [int(i) for i in text[1].split()]

filein.close()

if by1 <= ay1 and by2 >= ay2:
    if bx1 <= ax1 and ax1 <= bx2 <= ax2:
        area = (ax2 - bx2)*(ay2 - ay1)
    elif bx2 >= ax2 and ax1 <= bx1 <= ax2:
        area = (bx1 - ax1)*(ay2 - ay1)
    elif bx1 <= ax1 and bx2 >= ax2:
        area = 0
    else:
        area = (ax2-ax1)*(ay2-ay1)
elif bx1 <= ax1 and bx2 >= ax2:
    if by1 <= ay1 and ay1 <= by2 <= ay2:
        area = (ay2 - by2)*(ax2 - ax1)
    elif by2 >= ay2 and ay1 <= by1 <= ay2:
        area = (by1 - ay1)*(ax2 - ax1)
    else:
        area = (ax2-ax1)*(ay2-ay1)
else:
    area = (ax2-ax1)*(ay2-ay1)

fileout.write(str(area) + '\n')
fileout.close()
