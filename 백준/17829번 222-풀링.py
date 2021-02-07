def divide_222(graph, n):
    result = []
    for i in range(0, n, 2):
        tmp = []
        for j in range(0, n, 2):
            divided = [graph[i][j], graph[i][j + 1], graph[i + 1][j], graph[i + 1][j + 1]]
            divided.pop(divided.index(max(divided)))
            a = max(divided)
            tmp.append(a)
        result.append(tmp)
    
    graph = result
    return graph



n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

while n > 1:
    graph = divide_222(graph, n)
    n //= 2

print(graph[0][0])
