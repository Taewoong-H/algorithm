n = int(input())

explorer = list(map(int, input().split()))
explorer.sort()
answer = 0
count = 0

for i in explorer:
    count += 1
    if i <= count:
        answer += 1
        count = 0

print(answer)
