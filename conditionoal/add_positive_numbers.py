sum_positive = 0
while True:
    num = int(input())
    if num > 0:
        sum_positive += num
    else:
        print(sum_positive)
        break
