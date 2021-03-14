#  거스름돈 계산기
def calculate_change(payment, cost):
    change = payment - cost

    #계산
    fifty_count = int(change / 50000)
    ten_count = int(change % 50000) / 10000
    five_count = int(change % 10000) / 5000
    one_count = int(change % 5000) / 1000

    #답
    print("50000원 지폐: %d장" % fifty_count)
    print("10000원 지폐: %d장" % ten_count)
    print("5000원 지폐: %d장" % five_count)
    print("1000원 지폐: %d장" % one_count)

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)