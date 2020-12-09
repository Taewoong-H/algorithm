# BFS로 탐색하면서 가장 작은 수의 먹을 수 있는 물고기 먹고 상어 몸무게 증가시키고 초기화 시킨후 다시 BFS
from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)
shark = 2
eat = 0
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_distance = 0


def can_go(n, total_distance):
    global start
    can_eat = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                start = (i, j)
                distance[i][j] = total_distance
            if graph[i][j] != 9 and graph[i][j] < shark and graph[i][j] > 0:
                can_eat.append((i, j))
            if graph[i][j] != 9 and graph[i][j] <= shark:
                distance[i][j] = 0
    return can_eat


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if distance[nx][ny] == INF:
                continue
            if distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


n = int(input())

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

while True:
    distance = [[INF] * n for _ in range(n)]

    can_eat = can_go(n, total_distance)

    if len(can_eat) == 0:
        break

    bfs(start[0], start[1])
    min_distance = []
    for i in can_eat:
        min_distance.append((distance[i[0]][i[1]], i[0], i[1]))

    min_distance.sort(key=lambda x: (x[0], x[1], x[2]))
    for i in min_distance:
        if i[0] != 0:
            total_distance = i[0]
            graph[i[1]][i[2]] = 9
            break

    graph[start[0]][start[1]] = 0

    eat += 1
    if eat == shark:
        shark += 1
        eat = 0

print(total_distance)
