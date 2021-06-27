import sys

text = sys.stdin.readlines()
alphabet = text[0].strip()
letters = text[1].strip()

answer = 1
for letter in range(1,len(letters)):
    prev = alphabet.index(letters[letter-1])
    now = alphabet.index(letters[letter])
    if now in range(0,prev+1):
        answer += 1

sys.stdout.write(str(answer) + '\n')
