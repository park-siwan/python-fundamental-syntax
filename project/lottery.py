from random import randint


# 참가자 번호 추첨, 당첨자 번호 추첨, 속성: 1~45 랜덤, 서로 다름, 오름차순 정렬
def generate_numbers():
    numbers = []
    while len(numbers) < 6:
        num = randint(1, 46)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()

    return numbers


# 보너스를 포함한 리스트를 리턴
def draw_winning_numbers():
    numbers = generate_numbers()
    winning_numbers = generate_numbers()
    count = count_matching_numbers(numbers, winning_numbers)
    print("맞춘 횟수: ", count)

    bonus_numbers = list(winning_numbers)
    while len(bonus_numbers) < 7:
        bonus_number = randint(1, 46)
        if bonus_number not in bonus_numbers:
            bonus_numbers.append(bonus_number)

    print("보너스 번호:", bonus_number)
    check(numbers, bonus_numbers, count)

    return bonus_numbers


# list1과 list2 사이의 겹치는 번호 개수(1~6)를 리턴
def count_matching_numbers(list1, list2):
    i = 0
    count = 0
    while i < len(list1) - 1:
        if list1[i] in list2:
            count = count + 1
        i = i + 1
    return count


#  일치하는 번호 개수 만큼 상금을 리턴 (참가자의 번호6개, 당첨 번호)
def check(numbers, winning_numbers, count):
    print('check on', numbers, winning_numbers)
    bonus_number = winning_numbers[-1]

    # 보너스 체크하기
    bonus_count = 0
    if bonus_number in numbers:
        bonus_count = bonus_count + 1
    print('맞춘 보너스 횟수 :', bonus_count)

    # 상금 체크 후 출력하기
    count = count
    if count == 6 or count + bonus_count == 7:
        print('10억')
        return 1000000000
    elif count + bonus_count == 6:
        print('5천만')
        return 50000000
    elif count + bonus_count == 5:
        print('100만원')
        return 1000000
    elif count + bonus_count == 4:
        print('5만원')
        return 50000
    elif count + bonus_count == 3:
        print('5천원')
        return 5000
    else:
        print('상금없음')

draw_winning_numbers()
