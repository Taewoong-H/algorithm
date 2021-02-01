import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
count = 1

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in cave_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


while True:
    n = int(input())
    if n == 0:
        break

    cave = []
    for i in range(n):
        cave.append(list(map(int, input().split())))
    
    # 행렬을 인접 리스트로 만들기 위해 번호 지정
    graph = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
            graph[i][j] = cnt

    # 인접행렬로 만들기...
    cave_list = [[] for i in range(n**2 + 1)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i == 0:
                # 왼쪽에서 오는거
                cave_list[graph[i][j - 1]].append((graph[i][j], cave[i][j]))
                cave_list[graph[i][j]].append((graph[i][j - 1], cave[i][j - 1]))
            elif j == 0:
                # 위에서 오는거
                cave_list[graph[i - 1][j]].append((graph[i][j], cave[i][j]))
                cave_list[graph[i][j]].append((graph[i - 1][j], cave[i - 1][j]))
            else:
                # 왼쪽
                cave_list[graph[i][j - 1]].append((graph[i][j], cave[i][j]))
                cave_list[graph[i][j]].append((graph[i][j - 1], cave[i][j - 1]))
                # 오른쪽
                cave_list[graph[i - 1][j]].append((graph[i][j], cave[i][j]))
                cave_list[graph[i][j]].append((graph[i - 1][j], cave[i - 1][j]))

    distance = [INF] * (n**2 + 1)
    
    dijkstra(1)

    print("Problem {0}: {1}".format(count, distance[n**2] + cave[0][0]))

    count += 1