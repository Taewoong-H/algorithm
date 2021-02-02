# dp[i] = dp[i - 1] + dp[i - m]
N, M = map(int, input().split())

dp = [0] * 10001

dp[1] = 1
if M != 1:
    for i in range(1, M):
        dp[i] = 1

    dp[M] = 2

for i in range(M + 1, N + 1):
    dp[i] = (dp[i - 1] + dp[i - M])

print(dp[N] % 1000000007)