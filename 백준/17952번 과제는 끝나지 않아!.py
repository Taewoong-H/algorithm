import sys
input = sys.stdin.readline

n = int(input())

stack = []
score = 0

for i in range(n):
    assignment = list(map(int, input().split()))
    if assignment[0] == 1:
        new_assignment = [assignment[1], assignment[2] - 1]
        stack.append(new_assignment)
        if stack[-1][1] == 0:
            score += stack[-1][0]
            stack.pop()

    else:
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                score += stack[-1][0]
                stack.pop()
        else:
            continue

print(score)
