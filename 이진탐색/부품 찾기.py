import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if mid == target:
            return mid
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_array = sorted(array)

for i in range(m):
    item = customer[i]
    result = binary_search(sorted_array, item, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
