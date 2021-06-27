filein = open('sleepy.in','r')
fileout = open('sleepy.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())

order = [int(cow) for cow in text[0].split()]

filein.close()

moves = 0

while True:
    sortedorder = order[:]
    sortedorder.sort()
    if sortedorder == order:
        break
    front = order.pop(0)
    moves += 1
    for index in range(1,N):
        neworder = order[:index] + [front] + order[index:]
        checksort = neworder[index:]
        checksort.sort()
        if neworder[index:] == checksort:
            order = neworder
            break

fileout.write(str(moves) + '\n')
fileout.close()
