import copy

def solution(n, info):
    graph = [[1,2,3,4,5,6,7,8,9,10], [2,3,4,5,6,7,8,9,10], [3,4,5,6,7,8,9,10], [4,5,6,7,8,9,10], [5,6,7,8,9,10], [6,7,8,9,10], [7,8,9,10], [8,9,10], [9,10], [10], []]
    answer = [0] * 11
    dfs(graph, 0, n, info, answer)

    return answer

def dfs(graph, v, n, info, answer):
    
    if n == 0:
        print(answer)
        return False
    for i in graph[v]:
        answer[i] = info[i] + 1
        dfs(graph, i, n - 1, info, answer)
        answer[i] = 0
        
solution(5, [2,1,1,1,0,0,0,0,0,0,0])