import sys
from collections import deque

input = sys.stdin.readline

cursorLeft = deque()
cursorRight = deque()

n = input().strip()
m = int(input())

for i in n:
    cursorLeft.append(i)


for i in range(m):
    order = list(map(str, input().split()))
    if order[0] == 'P':
        cursorLeft.append(order[1])
    elif order[0] == 'L':
        if len(cursorLeft) == 0:
            continue
        else:
            cursorRight.appendleft(cursorLeft.pop())
    elif order[0] == 'D':
        if len(cursorRight) == 0:
            continue
        else:
            cursorLeft.append(cursorRight.popleft())
    elif order[0] == 'B':
        if len(cursorLeft) == 0:
            continue
        else:
            cursorLeft.pop()


result = cursorLeft + cursorRight

for i in result:
    print(i, end='')
