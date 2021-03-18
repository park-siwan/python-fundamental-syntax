in_file = open('data/household_book.txt', 'r', encoding='UTF-8')

# 총 매출
sum = 0

# 줄 세기
line_count = 0

# 파일의 각 줄 읽기
for line in in_file:
    data = line.strip().split(': ')
    amount = int(data[1])

    # 각 날의 매출을 총 매출에 추가
    sum = sum + amount

    line_count = line_count + 1

print(sum / line_count)

in_file.close()