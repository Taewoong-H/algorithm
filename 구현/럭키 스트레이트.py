n = int(input())
s = str(n)
mid = len(s) // 2
left = 0
right = 0

for i in range(mid):
    left += int(s[i])

for i in range(mid, len(s)):
    right += int(s[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
