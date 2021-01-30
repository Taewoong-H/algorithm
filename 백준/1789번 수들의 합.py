s = int(input())
count = 0
tmp = 1

while s > 0:
    s -= tmp
    if s < 0:
        break
    count += 1
    tmp += 1

print(count)
        