n = int(input())
a = input().split()

x, y = 1, 1
command = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in a:
  for index in range(len(command)):
    if i == command[index]:
      x += dx[index]
      y += dy[index]
    if x > n or y > n or x < 1 or y < 1:
      x -= dx[index]
      y -= dy[index]

print(x, y)