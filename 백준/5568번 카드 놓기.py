import itertools

n = int(input())
k = int(input())
card = []

for _ in range(n):
    card.append(input())

nPr = itertools.permutations(card, k)
list_nPr = list(nPr)

answer = []
for i in list_nPr:
    answer.append(''.join(i))

print(len(set(answer)))
