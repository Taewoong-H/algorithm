s = input()
num = 0
alphabet = []

for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        num += int(i)
    else:
        alphabet.append(i)

alphabet.sort()

answer = ''
for i in alphabet:
    answer += i

if num != 0:
    answer += str(num)

print(answer)
