numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for left_index in range(int(len(numbers) / 2)):
    # 오른쪽 인덱스 계산
    right_index = len(numbers) - left_index - 1

    # 원소 바꾸기
    temp = numbers[left_index]
    numbers[left_index] = numbers[right_index]
    numbers[right_index] = temp

print("뒤집어진 리스트: " + str(numbers))