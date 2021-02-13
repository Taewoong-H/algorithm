n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input()))

chess = ["W", "B"]
chess_board_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
chess_board_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

result = n * m
for i in range(0, n - 7):
    for j in range(0, m - 7):
        W_result = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if board[x][y] != chess_board_W[x - i][y - j]:
                    W_result += 1
        result = min(result, W_result)

for i in range(0, n - 7):
    for j in range(0, m - 7):
        B_result = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if board[x][y] != chess_board_B[x - i][y - j]:
                    B_result += 1
        result = min(result, B_result)
print(result)