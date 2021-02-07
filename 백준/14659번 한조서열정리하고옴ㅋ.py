n = int(input())

mount = list(map(int, input().split()))

result = 0
count = 0
max_mount = 0
for i in mount:
    if i > max_mount:
        max_mount = i
        count = 0
    else:
        count += 1
    result = max(result, count)


print(result)