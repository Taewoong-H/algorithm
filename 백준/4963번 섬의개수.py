import sys
sys.setrecursionlimit(1000000)


def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if island[x][y] == 1:
        island[x][y] = 0
        # 상하좌우
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        # 대각선
        dfs(x - 1, y - 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        return True
    return False


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = []
    for i in range(h):
        island.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1

    print(result)
