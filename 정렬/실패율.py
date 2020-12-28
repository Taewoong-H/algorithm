def solution(N, stages):
    failure = []

    for i in range(1, N + 1):
        onStageUser = 0
        onStageButNotClearUser = 0

        for j in stages:
            if j > i:
                onStageUser += 1
            elif j == i:
                onStageUser += 1
                onStageButNotClearUser += 1
        # 예외처리, 분모가 0이면 오류.
        if onStageUser == 0:
            failure.append([i, 0])
        else:
            failure.append([i, onStageButNotClearUser / onStageUser])
    # 실패율을 기준으로 내림차순 정렬
    failure.sort(reverse=True, key=lambda x: x[1])

    answer = []
    for i in failure:
        answer.append(i[0])

    return answer
