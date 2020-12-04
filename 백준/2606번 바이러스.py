def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


computer = int(input())
n = int(input())

parent = [0] * (computer + 1)

for i in range(1, computer + 1):
    parent[i] = i

result = 0

for i in range(n):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(2, computer + 1):
    if find_parent(parent, 1) == find_parent(parent, i):
        result += 1

print(result)
