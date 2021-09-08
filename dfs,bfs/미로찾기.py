# n,m 크기의 직사각형 형태의 미로
# 위치는 (1,1)에서 한칸씩 이동가능
# 괴물이 있는 부분은 0, 없는 부분은 1
# 괴물을 피해 이동해야함
# (n,m)출구로 이동하기 위한 가장 최소 거리
# 시작칸과 마지막칸은 항상 1
from collections import deque

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
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))