n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
countA = 0
countB = 0

while countA < n and countB < m:
    if B[countB] > A[countA]:
        countA += 1
    else:
        A[countA] -= B[countB]
        countB += 1

print(sum(A))
