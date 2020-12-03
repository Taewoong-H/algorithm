import heapq
import copy
import sys

input = sys.stdin.readline

n = int(input())
count = 0
subin = []

for i in range(n):
    result = []
    talk = int(input())
    heapq.heappush(subin, talk)
    a = copy.deepcopy(subin)
    for i in range(len(a)):
        result.append(heapq.heappop(a))
    start = 0
    end = len(result) - 1
    mid = (start + end) // 2
    print(result[mid])
