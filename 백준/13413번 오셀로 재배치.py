t = int(input())

for _ in range(t):
    n = int(input())
    init = input()
    goal = input()

    W_B = 0
    B_W = 0
    for i in range(n):
        if init[i] == 'W' and goal[i] == 'B':
            W_B += 1
        elif init[i] == 'B' and goal[i] == 'W':
            B_W += 1

    answer = (max(W_B, B_W) - min(W_B, B_W)) + min(W_B, B_W)

    print(answer)
