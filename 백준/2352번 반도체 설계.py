# dp로 풀면 시간초과
# 12015번 LIS2 와 같이 binary search로 풀어야 한다.
# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import bisect

n = int(input())

port = list(map(int, input().split()))

dp = [port[0]]

for i in range(n):
    if port[i] > dp[-1]:
        dp.append(port[i])
    else:
        index = bisect.bisect_left(dp, port[i])
        dp[index] = port[i]


print(len(dp))



