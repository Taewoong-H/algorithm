INF = int(1e9)

n, m = map(int, input().split())

grade = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    grade[a][b] = 1

for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            grade[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            grade[a][b] = min(grade[a][b], grade[a][k] + grade[k][b])

visited = [[]*(n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if grade[a][b] != INF:
            visited[a].append(b)
            visited[b].append(a)

for i in range(1, n + 1):
    visited[i] = set(visited[i])

answer = 0
for i in range(1, n + 1):
    if len(visited[i]) == n:
        answer += 1

print(answer)
