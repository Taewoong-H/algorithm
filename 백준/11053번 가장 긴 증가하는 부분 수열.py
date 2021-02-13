n = int(input())

dp = [1] * 1001

A = list(map(int, input().split()))


for i in range(len(A)):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))