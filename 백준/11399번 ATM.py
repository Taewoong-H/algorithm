n = int(input())

people = list(map(int, input().split()))

people.sort()

ATM = 0
sum_people = 0
for i in range(n):
    sum_people += people[i]
    ATM += sum_people

print(ATM)
