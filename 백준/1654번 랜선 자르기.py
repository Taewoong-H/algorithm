import sys
input = sys.stdin.readline

k, n = map(int, input().split())
array = []

for i in range(k):
    array.append(int(input()))

start = 0
end = max(array)

result = 1
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        total += x // mid

    if total >= n:
        start = mid + 1

    else:
        end = mid - 1


print(end)
