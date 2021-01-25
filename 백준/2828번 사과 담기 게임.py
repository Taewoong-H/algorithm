# 브론즈 맞나??? 왜케 어려워
n, m = map(int, input().split())
j = int(input())

basket = [1, 1 + m]
move = 0

for _ in range(j):
    apple = int(input())

    if apple >= basket[0] and apple < basket[1]:
        continue
    elif apple >= basket[1]:
        move += (apple + 1 - basket[1])
        basket[0] = (apple + 1) - m
        basket[1] = apple + 1
    elif apple <= basket[0]:
        move += (basket[0] - apple)
        basket[0] = apple
        basket[1] = apple + m

print(move)
