n = int(input())
student = []

for i in range(n):
    n, k, e, m = map(str, input().split())
    n = chr(n)
    k = int(k)
    e = int(e)
    m = int(m)
    student.append((n, k, e, m))


s = sorted(student, key=lambda k: (-k[1], k[2], -k[3], k[0]))

print(s)
