def pow_matrix(x, y):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k] * y[k][j]
                result[i][j] %= 1000

    return result


n, b = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 분할정복..

answer = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

while b != 1:
    tmp = matrix[:]
    if b % 2:
        answer = pow_matrix(answer, tmp)
        b -= 1
    else:
        matrix = pow_matrix(tmp, tmp)
        b //= 2

answer = pow_matrix(answer, matrix)
for i in answer:
    print(*i)
