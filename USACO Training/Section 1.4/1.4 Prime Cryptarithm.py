'''
ID: pranjal16
LANG: PYTHON3
TASK: crypt1
'''

filein = open('crypt1.in','r')
fileout = open('crypt1.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

numbers = text[0].split()
for n in range(N):
    numbers[n] = int(numbers[n])

filein.close()

twodigit = []
threedigit = []
fourdigit = []
for i in numbers:
    for j in numbers:
        if i != 0:
            twodigit.append(10*i + j)
        for k in numbers:
            if i != 0:
                threedigit.append(100*i + 10*j + k)

numsolutions = 0
for num1 in threedigit:
    for num2 in twodigit:
        if num1*num2//10 in threedigit and num1*num2 % 10 in numbers:
            a = num2//10
            b = num2 % 10
            if a*num1 in threedigit and b*num1 in threedigit:
                numsolutions += 1

fileout.write(str(numsolutions) + '\n')
fileout.close()
