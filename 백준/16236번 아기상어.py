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


# 시작점 찾기
def find_start(n, total_distance):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                start = (i, j)
                distance[i][j] = total_distance  # distance에 총 시간을 넣어서 축적시킴
    return start


# 갈수 있는 곳(distance)와 먹을 수 있는 곳(can_eat)를 bfs로 찾는다.
# 첨엔 순차 탐색으로 찾았는데, 틀렸었다. bfs로 찾아야 직접적으로 갈 수 있는 경로 상에 먹을 수 있는 물고기가 있는지 알 수 있다.
def can_go(x, y):
    can_eat = []
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > shark:  # 아기 상어보다 크면 못감
                continue
            if distance[nx][ny] == 0:  # 이미 간 경로
                continue
            if graph[nx][ny] != 9 and graph[nx][ny] < shark and graph[nx][ny] > 0:  # 아기 상어가 먹을 수 있는 물고기
                can_eat.append((nx, ny))
            if graph[nx][ny] != 9 and graph[nx][ny] <= shark:  # 아기상어가 갈 수 있는 경로 distance에 0으로 초기화
                distance[nx][ny] = 0
                queue.append((nx, ny))

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
                distance[nx][ny] = distance[x][y] + 1  # 상어가 갔으면 경로에 1초씩 더함
                queue.append((nx, ny))


n = int(input())

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

while True:
    # 상어가 갈 경로 INF로 초기화, bfs로 탐색해서 갈 수 있으면 0으로 초기화.
    distance = [[INF] * n for _ in range(n)]

    start = find_start(n, total_distance)
    can_eat = can_go(start[0], start[1])

    if len(can_eat) == 0:  # 더이상 먹을 수 있는 물고기가 없으면 종료
        break

    bfs(start[0], start[1])  # 모든 경로 다 가보기.
    min_distance = []  # 가장 짧은 거리 구하기.
    for i in can_eat:
        # 모든 시간과, 그 좌표를 넣음
        min_distance.append((distance[i[0]][i[1]], i[0], i[1]))

    # 시간을 첫번째로 정렬하여 젤 적은 시간을 구함.
    min_distance.sort(key=lambda x: (x[0], x[1], x[2]))
    for i in min_distance:
        if i[0] != 0:
            total_distance = i[0]  # 젤 적은 시간을 전체 시간에 넣음. distance는 계속 축적됨.
            graph[i[1]][i[2]] = 9  # 젤 적은 시간의 물고기를 먹고 그 지점이 시작점이 됨
            break

    graph[start[0]][start[1]] = 0  # 아까 전에 시작점은 0으로 초기화시킴.

    # 상어가 물고기를 먹었으니 부피를 키움
    eat += 1
    if eat == shark:
        shark += 1
        eat = 0

print(total_distance)
