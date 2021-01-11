N = input()

number = N.split('-')

for i in range(len(number)):
    number[i] = number[i].split('+')

    for j in range(len(number[i])):
        number[i][j] = int(number[i][j])
    number[i] = sum(number[i])

result = number[0]
for i in range(1, len(number)):
    result -= number[i]
print(result)
