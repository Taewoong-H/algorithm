from itertools import combinations

n = int(input())
state = [[0] * (n + 1)]
for _ in range(n):
    state.append([0] + list(map(int, input().split())))

member = [i for i in range(1, n + 1)]
pick = n//2

combination_list = list(combinations(member, pick))
teamA = combination_list[: len(combination_list)//2]
teamB = combination_list[-1: len(combination_list)//2 - 1: -1]

answer = int(1e9)
for x in range(len(teamA)):
    stateA = 0
    stateB = 0
    for i in range(0, pick - 1):
        for j in range(i + 1, pick):
            Ai = teamA[x][i]
            Aj = teamA[x][j]
            stateA += (state[Ai][Aj] + state[Aj][Ai])

            Bi = teamB[x][i]
            Bj = teamB[x][j]
            stateB += (state[Bi][Bj] + state[Bj][Bi])

    answer = min(abs(stateA - stateB), answer)
print(answer)
