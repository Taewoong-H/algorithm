n = int(input())

triangle = []

for i in range(n):
    tmp = list(map(int, input().split()))
    triangle.append(tmp)

dp = triangle.copy()

for i in range(1, n):
    for j in range(0, i + 1):
        if j != 0 and j != i:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
        elif j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]

print(max(dp[n - 1]))
