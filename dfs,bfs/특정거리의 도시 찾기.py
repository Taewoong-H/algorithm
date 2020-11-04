from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

queue = deque([x])
visited = [-1] * (n + 1)
visited[x] = 0

while queue:
    a = queue.popleft()
    for i in graph[a]:
        if visited[i] == -1:
            visited[i] = visited[a] + 1
            queue.append(i)


count = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        count = True

if count == False:
    print(-1)
