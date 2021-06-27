filein = open('cbarn.in','r')
fileout = open('cbarn.out','w')

text = filein.readlines()
n = int(text.pop(0).strip())
rooms = [int(i.strip()) for i in text]

filein.close()

mindistance = 10**100
for enter in range(n):
    newrooms = rooms[enter:] + rooms[:enter]
    distances = [newrooms[i]*i for i in range(n)]
    distance = sum(distances)
    if distance < mindistance:
        mindistance = distance

fileout.write(str(mindistance) + '\n')
fileout.close()
