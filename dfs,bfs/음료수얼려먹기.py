# N * M 크기의 얼음틀이 있다.
# 구멍은 0, 칸막이는 1
# 구멍이 뚫려있는 부분끼리는 연결되어 있어서 하나로 나옴

# N, M 입력
n, m = map(int, input().split())

# 그래프 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드 방문한 뒤에 연결된 모든 노드들 방문


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
