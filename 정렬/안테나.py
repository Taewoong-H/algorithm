n = int(input())
house = list(map(int, input().split()))
distance = 0

for i in house:
    distance += i

avg = distance/n
closet = []
for i in house:
    closet.append(abs(avg - i))

print(house[closet.index(min(closet))])
