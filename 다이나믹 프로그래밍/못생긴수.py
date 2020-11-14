n = int(input())

d = [0] * 1001
d[1] = 1
prime = [2, 3, 5]


for i in prime:
    for j in range(1, 1001):
        if j % i == 0 and d[j//i] == 1:
            d[j] = 1

count = 0
for i in range(len(d)):
    if d[i] == 1:
        count += 1
    if count == n:
        print(i)
        break
