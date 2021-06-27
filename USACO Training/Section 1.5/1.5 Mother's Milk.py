"""
ID: pranjal16
LANG: PYTHON3
TASK: milk3
"""

filein = open('milk3.in','r')
fileout = open('milk3.out','w')

text = filein.readlines()
text = text[0].split()
sizes = [int(text[i]) for i in range(3)]

filein.close()
states = []
initialstate = [0,0,sizes[2]]

def transfer(state,transfer):
    '''transfers milk from one bucket to another'''
    b1,b2 = transfer
    v1,v2 = state[b1],state[b2]
    max2 = sizes[b2]
    if v1 >= max2-v2:
        transferred = max2-v2
    else:
        transferred = v1
    
    newstate = [0,0,0]
    newstate[3-b1-b2] = state[3-b1-b2]
    newstate[b1] = v1 - transferred
    newstate[b2] = v2 + transferred
    return newstate

def findstates(state):
    '''find all states after state'''
    if state not in states:
        states.append(state)
        for i in range(3):
            for j in range(3):
                if i != j:
                    findstates(transfer(state,[i,j]))

findstates(initialstate)
sols = []
for state in states:
    if state[0] == 0:
        if state[2] not in sols:
            sols.append(state[2])

sols.sort()
sols = [str(i) for i in sols]
text = ' '.join(sols) + '\n'
fileout.write(text)

fileout.close()

