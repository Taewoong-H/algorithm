x = int(input())

d = [0] * 30001

# 탑다운


def dp(x):
    if x == 1:
        return 0

    if x % 2 == 0 and x % 3 == 0 and x % 5 == 0:
        d[x] = min(dp(x-1), dp(x//2), dp(x//3), dp(x//5)) + 1
    elif x % 3 == 0 and x % 5 == 0:
        d[x] = min(dp(x-1), dp(x//3), dp(x//5)) + 1
    elif x % 2 == 0 and x % 5 == 0:
        d[x] = min(dp(x-1), dp(x//2), dp(x//5)) + 1
    elif x % 2 == 0 and x % 3 == 0:
        d[x] = min(dp(x-1), dp(x//2), dp(x//3)) + 1
    elif x % 2 == 0:
        d[x] = min(dp(x-1), dp(x//2)) + 1
    elif x % 3 == 0:
        d[x] = min(dp(x-1), dp(x//2)) + 1
    elif x % 5 == 0:
        d[x] = min(dp(x-1), dp(x//5)) + 1
    else:
        d[x] = dp(x-1) + 1
    return d[x]


print(dp(x))
print(d[:x])

# 바텀업
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
print(d[:x])
