from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if new_graph[nx][ny] == 1:
                continue
            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = new_graph[x][y] + 1
                queue.append((nx, ny))
    return new_graph[n - 1][m - 1]


distance = []

for i in range(n):
    for j in range(m):
        new_graph = copy.deepcopy(graph)
        if new_graph[i][j] == 1:
            new_graph[i][j] = 0
            a = bfs(0, 0)
            if a != 0:
                distance.append(a)
                print(new_graph)
if len(distance) == 0:
    print(-1)
else:
    print(min(distance) + 1)
