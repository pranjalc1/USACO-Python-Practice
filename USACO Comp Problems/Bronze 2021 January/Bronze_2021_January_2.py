import sys

text = sys.stdin.readlines()
N = int(text.pop(0).strip())
IDS = [int(i) for i in text[0].split()]

even = [i for i in IDS if i % 2 == 0]
odd = [i for i in IDS if i % 2 == 1]
even = len(even)
odd = len(odd)

if odd > even:
    while odd != even + 1 and even != odd and even != odd + 1:
        odd -= 2
        even += 1
    if odd == even + 1:
        odd -= 2
    answer = even + odd
elif odd == even or even == odd + 1:
    answer = even + odd
else:
    while even != odd + 1:
        even -= 1
    answer = even + odd

sys.stdout.write(str(answer) + '\n')
