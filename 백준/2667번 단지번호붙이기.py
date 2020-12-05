n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return count
    return 0


result = 0
count = 0
count_result = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) > 0:
            result += 1
            count_result.append(count)
            count = 0

print(result)
count_result.sort()

for i in range(result):
    print(count_result[i])
