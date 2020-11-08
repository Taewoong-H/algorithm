n = int(input())
card = []
for i in range(n):
    card.append(int(input()))

card = sorted(card, reverse=True)

sum_card = card.pop()
answer = 0
while card:
    c = card.pop()
    sum_card += c
    answer += sum_card

print(answer)

# heapq를 이용해 다시풀기..
