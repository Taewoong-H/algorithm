def isPerfect(p):
    P = []
    for i in range(len(p)):
        if i == '(':
            P.append(i)
        else:
            if len(P) == 0:
                return False
            else:
                P.pop()
    return True

# 미완성
def solution(p):
    left = 0
    right = 0
    
    for i in range(len(p)):
        if i == '(':
            left += 1
        else:
            right += 1
    
    perfect = 0
    if left == right:
        
    answer = ''
    
    return answer