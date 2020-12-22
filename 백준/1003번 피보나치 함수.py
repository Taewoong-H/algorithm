t = int(input())

dp_zero = [0] * 41
dp_one = [0] * 41

dp_zero[0] = 1
dp_one[0] = 0

dp_zero[1] = 0
dp_one[1] = 1

for i in range(t):
    n = int(input())
    if (n == 0):
        print(dp_zero[0], dp_one[0])
    elif (n == 1):
        print(dp_zero[1], dp_one[1])

    else:
        for j in range(2, n + 1):
            dp_zero[j] = dp_zero[j - 1] + dp_zero[j - 2]
            dp_one[j] = dp_one[j - 1] + dp_one[j - 2]

        print(dp_zero[n], dp_one[n])
