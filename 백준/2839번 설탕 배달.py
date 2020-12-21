n = int(input())

salt = [3, 5]

dp = [5000] * (n + 1)

dp[0] = 0
for i in range(2):
    for j in range(salt[i], n + 1):
        if dp[j - salt[i]] != 5000:
            dp[j] = min(dp[j], dp[j - salt[i]] + 1)


if dp[n] == 5000:
    print(-1)
else:
    print(dp[n])
