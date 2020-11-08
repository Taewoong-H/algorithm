# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search_1(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search_1(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    else:
        return binary_search_1(array, target, mid + 1, end)


# 이진 탐색 소스코드 구현(반복문)
def binary_search_2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result_1 = binary_search_1(array, target, 0, n - 1)
result_2 = binary_search_2(array, target, 0, n - 1)
if result_1 == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result_1 + 1)

if result_2 == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result_2 + 1)
