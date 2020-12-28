def solution(s):
    answer = len(s)
    result = len(s)

    for i in range(1, len(s)//2 + 1):
        # 처음 비교 대상.
        standard = s[0:i]
        count = 1

        for j in range(0, len(s), i):
            # standard와 비교할 다음 것.
            compare = s[j+i:j+i+i]

            if standard == compare:
                count += 1
            else:
                # 연속되지 않으므로 standard 변경
                standard = compare
                # count가 1 일 경우 길이는 변하지 않으므로 1 이상일 경우
                if count > 1:
                    # 전체 길이에서 i * count(중복된 글자의 전체길이)를 빼고, len(str(count)) + i(압축된 문자의 길이)를 추가
                    result -= i * count
                    result += len(str(count)) + i
                # count 초기화
                count = 1

        if answer > result:
            answer = result
        # result 초기화
        result = len(s)

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))
