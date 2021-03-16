# 빈 리스트 만들기
numbers = []

# numbers 에 자연수 1부터 10까지 추가
i = 1
while i <= 10:
    numbers.append(i)
    i = i + 1
print(numbers)

# numbers 에서 홀수 제거
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 == 1:
        del numbers[i]
    i = i - 1
print(numbers)

# numbers 의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers 를 정렬해서 출력
print(sorted(numbers))