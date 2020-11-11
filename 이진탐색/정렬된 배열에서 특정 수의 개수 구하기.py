# mid값을 찾은 후 pop으로 list에서 제거, 후 다시 mid값 찾기
# pop(i)가 O(N)의 시간복잡도를 가져서 힘들것 같음
n, x = map(int, input().split())

array = list(map(int, input().split()))

start = array[0]
end = array[len(array) - 1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    if array[mid] == x:
        answer += 1
        array.pop(mid)  # 시간복잡도 pop(i) = O(N) 의 시간복잡도를 가지고 있음..
        end = array[len(array) - 1]
    elif array[mid] > x:
        end = mid - 1
    else:
        start = mid + 1

if answer == 0:
    print(-1)
else:
    print(answer)

# or
# 두번째 풀이방법
# mid값이 x값과 같은것을 찾고 [mid - i] [mid + i]로 중복된 값들 찾아나가기
n, x = map(int, input().split())

array = list(map(int, input().split()))

start = array[0]
end = array[len(array) - 1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    if array[mid] == x:
        answer += 1
        break
    elif array[mid] > x:
        end = mid - 1
    else:
        start = mid + 1

for i in range(1, n//2 + 1):
    if array[mid - i] == x:
        answer += 1
    else:
        break
for i in range(1, n//2 + 1):
    if array[mid + i] == x:
        answer += 1
    else:
        break

if answer == 0:
    print(-1)
else:
    print(answer)
