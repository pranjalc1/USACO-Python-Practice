import sys

text = sys.stdin.readlines()
ax1,ay1,ax2,ay2 = [int(i) for i in text[0].split()]
bx1,by1,bx2,by2 = [int(i) for i in text[1].split()]

horiz = max(ax2,bx2) - min(ax1,bx1)
vert = max(ay2,by2) - min(ay1,by1)
maxside = max(horiz,vert)

area = maxside**2
sys.stdout.write(str(area) + '\n')
