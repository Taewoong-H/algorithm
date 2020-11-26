from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    array = []

    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(queue.popleft())
        array.append(tmp)

    # 첫 시작이 가장 큰 값
    start = 0
    for i in range(n):
        if array[i][0] > start:
            start = i
    answer = array[start][0]

    for i in range(1, m):
        if start >= 1 and start < n - 1:
            answer += max(array[start][i], array[start - 1]
                          [i], array[start + 1][i])
            if max(array[start][i], array[start - 1]
                   [i], array[start + 1][i]) == array[start - 1][i]:
                start -= 1
            elif max(array[start][i], array[start - 1]
                     [i], array[start + 1][i]) == array[start + 1][i]:
                start += 1
        elif start < 1:
            answer += max(array[start][i], array[start + 1][i])
            if max(array[start][i], array[start + 1][i]) == array[start + 1][i]:
                start += 1
        else:
            answer += max(array[start][i], array[start - 1][i])
            if max(array[start][i], array[start - 1][i]) == array[start - 1][i]:
                start -= 1
    print(answer)
