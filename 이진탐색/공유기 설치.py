# 미해결

n, c = map(int, input().split())
home = []

for i in range(n):
    home.append(int(input()))

mid = max(home) // (c - 1)
start = min(home)
end = max(home)
