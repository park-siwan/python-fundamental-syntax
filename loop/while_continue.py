i = 0
while i < 15:
    i = i + 1

    # i가 홀수면 print(i) 안하고 바로 조건부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)
