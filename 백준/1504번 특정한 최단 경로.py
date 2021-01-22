import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for i in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


fst = dijkstra(1)
sec = dijkstra(v1)
trd = dijkstra(v2)

total_distance = min(fst[v1] + sec[v2] + trd[n], fst[v2] + trd[v1] + sec[n])

if total_distance < INF:
    print(total_distance)
else:
    print(-1)
