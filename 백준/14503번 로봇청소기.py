from collections import deque

n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = 0
answer = 0
# 북, 동, 남, 서
direction = [0, 1, 2, 3]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((r, c))

while q:
    x, y = q.popleft()
    if graph[x][y] == 0:
        graph[x][y] = 1
        answer += 1
        # for i in range(n):
        #     for j in range(m):
        #         print(graph[i][j], end="")
        #     print("")
        # print("\n")

    nd = d - 1
    if nd < 0:
        nd = 3
    
    nx = x + dx[nd]
    ny = y + dy[nd]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 1:
        d = nd
        count += 1
        if count == 4:
            nx = x - dx[d]
            ny = y - dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            q.append((nx, ny))
            count = 0
        else:
            q.append((x, y))
    else:
        d = nd
        count = 0
        q.append((nx, ny))

print(answer)