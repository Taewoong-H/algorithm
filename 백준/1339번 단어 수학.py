# 다시풀기

n = int(input())
alphabets = []
words = []
word_to_num = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
               "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
greedy_num = 9

for _ in range(n):
    word = input()
    alphabets.append(word)
    for i in range(len(word)):
        words.append((len(word) - i, word[i]))

words.sort(reverse=True, key=lambda x: x[0])

for i in words:
    for j in word_to_num:
        if i[1] == j:
            if word_to_num[j] == 0:
                word_to_num[j] = greedy_num
                greedy_num -= 1

alphabet_to_num = ""
num = []
for alphabet in alphabets:
    for i in alphabet:
        for j in word_to_num:
            if i == j:
                alphabet_to_num += str(word_to_num[j])
    num.append(alphabet_to_num)
    alphabet_to_num = ""

answer = 0
for i in num:
    answer += int(i)
print(answer)
