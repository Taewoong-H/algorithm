# 점 하나도 크기를 1로 친다... 어이없네

N, M = map(int, input().split())

rect = []
max_size = 1

# 연결된 숫자를 배열의 형태로 넣기 위해..
for _ in range(N):
    col = list(input())
    col = list(map(int, col))
    rect.append(col)

# 정사각형의 변의 길이를 1부터 min(N, M)까지 정해서 살펴본다
for a in range(1, min(N, M)):
    # 가로 기준점. 0부터 변의 길이(a)를 뺀 위치까지 살펴본다.
    for i in range(N - a):
        # 세로 기준점
        for j in range(M - a):
            first = rect[i][j]
            # 기준점으로부터 변의 길이를 더한 각 정사각형 꼭지점이 같으면 정사각형
            if first == rect[i + a][j] and first == rect[i][j + a] and first == rect[i + a][j + a]:
                # 젤 큰 넓이를 저장
                max_size = max((a + 1) ** 2, max_size)

print(max_size)
