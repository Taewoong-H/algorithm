n = int(input())
card = []
for i in range(n):
    card.append(int(input()))

card = sorted(card, reverse=True)
print(card)
sum_card = card.pop()
answer = 0
while card:
    c = card.pop()
    sum_card += c
    answer += sum_card

print(answer)
