import re

def solution(new_id):

    new_id = firstStep(new_id)
    new_id = secondStep(new_id)
    new_id = thirdStep(new_id)
    new_id = fourthStep(new_id)
    new_id = fifthStep(new_id)
    new_id = sixthStep(new_id)
    new_id = seventhStep(new_id)
    answer = new_id
    return answer

def firstStep(id):
    for i in id:
        if ord(i) >= 65 and ord(i) <= 90:
            id = id.replace(i, chr(ord(i) + 32))
    return id

def secondStep(id):
    new_id = id
    for i in id:
        if ord(i) == 46 or ord(i) == 95 or ord(i) == 45 or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
            continue
        else:
            new_id = new_id.replace(i, "")
    return new_id

def thirdStep(id):
    new_id = id
    new_id = re.sub("[.]{2,}", ".", new_id)
    return new_id

def fourthStep(id):
    id = id.strip('.')
    return id

def fifthStep(id):
    if id == '':
        id = 'a'
    return id

def sixthStep(id):
    if len(id) >= 16:
        id = id[:15]
    id = id.strip('.')
    return id

def seventhStep(id):
    while True:   
        if len(id) <= 2:
            id += id[-1]
        else:
            break
    return id

# 시작
print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
print(solution('=.='))
print(solution('123_.def'))
print(solution('abcdefghijklmn.p'))