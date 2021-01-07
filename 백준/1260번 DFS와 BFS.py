from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def dfs(graph, now, visited):
    visited[now] = True
    print(now, end=' ')

    for i in graph[now]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited_dfs)
print('')
bfs(graph, v, visited_bfs)
