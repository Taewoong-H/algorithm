import sys
input = sys.stdin.readline

N = int(input())
RGB = []
for i in range(N):
    RGB.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    for j in range(3):
        if(i == 0):
            dp[i][j] = RGB[i][j]
        else:
            if(j == 0):
                dp[i][j] = min(RGB[i][j]+dp[i-1][j+1], RGB[i][j]+dp[i-1][j+2])
            elif(j == 1):
                dp[i][j] = min(RGB[i][j]+dp[i-1][j-1], RGB[i][j]+dp[i-1][j+1])
            else:
                dp[i][j] = min(RGB[i][j]+dp[i-1][j-1], RGB[i][j]+dp[i-1][j-2])

print(min(dp[N-1]))
