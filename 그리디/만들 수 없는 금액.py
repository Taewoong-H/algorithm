n = int(input())
coin = list(map(int, input().split()))

coin.sort(reverse=True)

sum_coin = [0]

while coin:
    i = coin.pop()
    for j in range(len(sum_coin)):
        sum_coin.append(i + sum_coin[j])

for i in range(max(sum_coin)):
    if i not in sum_coin:
        print(i)
        break
