import itertools

n, m = map(int, input().split())

ball = list(map(int, input().split()))

total = list(itertools.combinations(ball, 2))
total_length = len(total)

for i in range(total_length):
    if total[i][0] == total[i][1]:
        total_length -= 1

print(total_length)
