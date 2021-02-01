

def Kantore(start, end, range):
    if range == 1:
        line[start] = '-'
        return
    
    new_range = range // 3
    Kantore(start, start + new_range - 1, new_range)
    Kantore(end - new_range + 1, end, new_range)

while True:
    try:
        N = int(input())
        n = 3**N
        line = [' ' for _ in range(n)]
        
        Kantore(0, n - 1, n)
        for i in range(n):
            print(line[i], end='')
        print()
    except EOFError:
        break