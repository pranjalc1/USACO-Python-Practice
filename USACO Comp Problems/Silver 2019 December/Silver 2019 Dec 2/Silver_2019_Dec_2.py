filein = open('meetings.in','r')
fileout = open('meetings.out','w')

text = filein.readlines()

for line in range(len(text)):
    text[line] = text[line].split()
    for term in range(len(text[line])):
        text[line][term] = int(text[line][term])

N = text[0][0]
L = text[0][1]

filein.close()

class Cow():
    '''class for a cow'''

    def __init__(self,num,w,x,d):
        '''Cow(cownum,w,x,d) --> Cow
        creates a Cow class
        num: cow number
        w: weight
        x: original distance from origin
        d: velocity'''

        self.num = num
        self.dist = x
        self.vel = d
        self.weight = w
        self.time = 0
        self.stop = False

    def move(self):
        '''Cow.move()
        moves the cow'''
        self.dist += self.vel
        if self.dist == 0 or self.dist == 2*L:
            self.vel = 0
            self.stop = True

    def rev_vel(self):
        '''Cow.rev_vel()
        reverses the velocity of the cow'''
        self.vel = -self.vel

    def get_num(self):
        '''Cow.get_num()
        gets cow's number'''
        return self.num

    def get_dist(self):
        '''Cow.get_dist()
        gets cow's distance from the origin'''
        return self.dist

    def get_weight(self):
        '''Cow.get_weight()
        gets cow's weight'''
        return self.weight
    
    def get_stop(self):
        '''Cow.get_stop() --> bool'''
        return self.stop

    def __eq__(self,second):
        '''checks if it is the same cow'''
        return self.get_num() == second.get_num()

cows = []

for cow in range(1,N+1):
    cows += [Cow(cow,text[cow][0],2*text[cow][1],text[cow][2])]

done = False
meetnumber = 0
while not done:
    for cow in cows:
        cow.move()

    for d in range(1,2*L):
        possiblecows = []
        for cow in range(N):
            if cows[cow].get_dist() == d:
                possiblecows += [cow]
            if len(possiblecows) == 2:
                break
        if len(possiblecows) == 2:
            for cow in possiblecows:
                cows[cow].rev_vel()
            meetnumber += 1

    weightstopped = sum([cow.get_weight() for cow in cows if cow.get_stop()])
    totalweight = sum([cow.get_weight() for cow in cows])
    
    if weightstopped >= 1/2*totalweight:
        done = True

fileout.write(str(meetnumber) + '\n')
fileout.close()
