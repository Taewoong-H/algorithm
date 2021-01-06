import sys

input = sys.stdin.readline

n = int(input())
stair = [0]
dp = [0] * (n + 1)
count = 1

for _ in range(n):
    stair.append(int(input()))

# dp 1번째 설정
dp[1] = stair[1]

for i in range(2, n + 1):
    if count < 2:
        # 이전에 두번 밟지 않았다면 점화식에 따라 dp[i-1]과 dp[i-2]중 더 큰것과 계단 값을 더한 값이 dp[i]가 됨
        dp[i] = max(stair[i] + dp[i - 1], stair[i] + dp[i - 2])
        count += 1
    else:
        # 이제 연속으로 두번 밟게 되었을 때가 두개의 경우로 나뉜다.
        # 1. 한칸 건너뛰고 밟고 온게 큰지 (예: 1번 밟고, 2번 건너뛰고, 3번밟음)
        # 2. 아니면 그전에 한칸 건너뛰고 두번 연속으로 밟고 온게 큰지 (예: 1번 건너뛰고, 2번 밟고, 3번 밟음)
        # 이 둘을 비교하면 된다.
        if stair[i] + dp[i - 2] < stair[i] + stair[i - 1] + dp[i - 3]:  # case 2
            dp[i] = stair[i] + stair[i - 1] + dp[i - 3]
            count = 2  # 두번 연속해서 밟았으니 count값을 2로
        else:  # case 1
            dp[i] = stair[i] + dp[i - 2]
            count = 1

print(dp[n])
