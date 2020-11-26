

def binary_search(a, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == mid:
            return mid
        elif a[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
a = list(map(int, input().split()))

start = 0
end = len(a) - 1

result = binary_search(a, start, end)
if result == None:
    print(-1)
else:
    print(result)
