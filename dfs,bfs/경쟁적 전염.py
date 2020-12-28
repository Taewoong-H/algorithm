from collections import deque


def find_virus():
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                virus.append(graph[i][j])

    virus.sort()
    return virus


def find_coord(virus):
    coord = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == virus:
                coord.append([i, j])

    return coord


def bfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > 0:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]


n, k = map(int, input().split())
graph = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = find_virus()
for _ in range(s):
    for i in virus:
        coord = find_coord(i)
        for j in coord:
            bfs(j[0], j[1])

print(graph[x - 1][y - 1])
