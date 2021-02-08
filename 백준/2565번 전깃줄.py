# LIS(가장 긴 증가하는 부분 수열)
n = int(input())

line = [0] * 501

for _ in range(n):
    a, b = map(int, input().split())    
    line[a] = b


dp = [0] * 501

for i in range(501):
    for j in range(i):
        if line[i] > line[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(n - max(dp))

