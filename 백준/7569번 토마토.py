from collections import deque
import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

box = [[[0] * (n) for _ in range(m)] for _ in range(h)]

for i in range(h):
    for j in range(m):
        tomato = list(map(int, input().split()))
        box[i][j] = tomato

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def find_ripe_tomate(n, m, h):
    queue = deque()
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if box[z][y][x] == 1:
                    queue.append((x, y, z))

    return queue


def bfs(x, y, z):

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if box[nz][ny][nx] == -1:
            continue
        if box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[z][y][x] + 1
            ripe_tomate.append((nx, ny, nz))

    return


def find_max_tomato(n, m, h):
    max_tomato = 0
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if box[z][y][x] > max_tomato:
                    max_tomato = box[z][y][x]
                if box[z][y][x] == 0:
                    return 0
    return max_tomato


ripe_tomate = find_ripe_tomate(n, m, h)

while ripe_tomate:
    x, y, z = ripe_tomate.popleft()
    bfs(x, y, z)

max_tomato = find_max_tomato(n, m, h)
if max_tomato == 0:
    print(-1)
else:
    print(max_tomato - 1)
