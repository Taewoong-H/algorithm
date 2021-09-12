import itertools

def solution(orders, course):
    answer = []
    for i in course:
        hashmap = {}
        for order in orders:
            if len(order) >= i:
                orderlist = list(order)
                orderlist.sort()
                nCr = itertools.combinations(orderlist, i)
                for j in list(nCr):
                    menu = "".join(j)
                    if (menu in list(hashmap.keys())):
                        hashmap[menu] += 1
                    else:
                        hashmap[menu] = 1      
            else:
                continue
        if (len(hashmap) > 0): 
            max_value = max(hashmap.values())
            if (max_value > 1):   
                for k in hashmap.items():
                    if (k[1] == max_value):
                        answer.append(k[0])
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))