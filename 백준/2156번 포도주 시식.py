# 2579번 계단오르기랑 비슷한 문제
n = int(input())
wine = [0]
dp = [0] * (n + 1)

for _ in range(n):
    wine.append(int(input()))

for i in range(1, n + 1):
    if i == 1:
        dp[1] = wine[1]
    elif i == 2:
        dp[2] = wine[2] + wine[1]
    else:
        dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i],
                    dp[i - 2] + wine[i], dp[i - 1])  # <= 계단문제랑 비슷한줄 알았는데 i번째를 안먹는 경우도 쳐야한다..

print(max(dp))
