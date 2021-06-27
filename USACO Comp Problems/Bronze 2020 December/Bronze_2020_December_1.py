import sys

text = sys.stdin.readlines()
numbers = [int(i) for i in text[0].split()]
numbers.sort()

A = numbers[0]
B = numbers[1]
C = numbers[-1] - A - B

answer = str(A) + ' ' + str(B) + ' ' + str(C) + '\n'
sys.stdout.write(answer)
