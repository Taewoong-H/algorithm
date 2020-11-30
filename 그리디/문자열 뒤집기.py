s = input()

reverse_1 = 0
for i in range(len(s) - 1):
    if s[i] == '1':
        if s[i + 1] == '0':
            reverse_1 += 1
        elif i + 1 == len(s) - 1 and s[i + 1] == '1':
            reverse_1 += 1

reverse_0 = 0
for i in range(len(s) - 1):
    if s[i] == '0':
        if s[i + 1] == '1':
            reverse_0 += 1
        elif i + 1 == len(s) - 1 and s[i + 1] == '0':
            reverse_0 += 1

print(min(reverse_1, reverse_0))
