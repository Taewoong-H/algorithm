def divide1(N, paper):
    paper1 = [[0] * (N // 2) for _ in range(N // 2)]
    for i in range(0, N // 2):
        for j in range(0, N // 2):
            paper1[i][j] = paper[i][j]
    return paper1


def divide2(N, paper):
    paper2 = [[0] * (N // 2) for _ in range(N // 2)]
    for i in range(0, N // 2):
        for j in range(N // 2, N):
            paper2[i][j - N//2] = paper[i][j]
    return paper2


def divide3(N, paper):
    paper3 = [[0] * (N // 2) for _ in range(N // 2)]
    for i in range(N // 2, N):
        for j in range(0, N // 2):
            paper3[i - N//2][j] = paper[i][j]
    return paper3


def divide4(N, paper):
    paper4 = [[0] * (N // 2) for _ in range(N // 2)]
    for i in range(N // 2, N):
        for j in range(N // 2, N):
            paper4[i - N//2][j - N//2] = paper[i][j]
    return paper4


def cut(paper, N):
    global white, blue
    for i in range(N):
        for j in range(N):
            if paper[0][0] != paper[i][j]:
                cut(divide1(N, paper), N//2)
                cut(divide2(N, paper), N//2)
                cut(divide3(N, paper), N//2)
                cut(divide4(N, paper), N//2)
                return
    if paper[0][0] == 1:
        blue += 1
    else:
        white += 1


N = int(input())
paper = []
white = 0
blue = 0

for _ in range(N):
    paper.append(list(map(int, input().split())))

cut(paper, N)
print(white, blue)
