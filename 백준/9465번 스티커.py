t = int(input())

for _ in range(t):
    n = int(input())

    sticker = []
    dp = [[0] * (n + 1) for _ in range(2)]

    for _ in range(2):
        sticker.append(list(map(int, input().split())))

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]

    for i in range(2, n):
        dp[0][i] = max(sticker[0][i] + dp[1][i - 1],
                       sticker[0][i] + dp[1][i - 2])
        dp[1][i] = max(sticker[1][i] + dp[0][i - 1],
                       sticker[1][i] + dp[0][i - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))
