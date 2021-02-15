n = int(input())

end_number = 0
count = 0
while True:
    end_number += 1
    string_end_number = str(end_number)
    if "666" in string_end_number:
        count += 1

        if count == n:
            print(end_number)
            break