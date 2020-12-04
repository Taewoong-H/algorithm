import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


input = sys.stdin.readline


n = int(input())

listA = list(map(int, input().split()))
listA.sort()

m = int(input())

listB = list(map(int, input().split()))

for i in range(m):
    answer = binary_search(listA, listB[i], 0, n - 1)
    if answer == None:
        print(0)
    else:
        print(1)
