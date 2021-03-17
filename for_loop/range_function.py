#  1부터 10까지 for 문을 돌리려는데 귀찮으니 range 를 쓰자.
#  range(n, m)은 n부터 m - 1 까지의 수이다.
for i in range(1, 11):
    print(i)  # 1 ~ 10 출력됨

# 0 부터 m - 1 까지 출력
for i in range(11):
    print(i)  # 0 ~ 10 출력됨

# range(n, m, s)은 n부터 m - 1 까지의 수 중 간격이 s인 수를 의미.
for i in range(3, 17, 3):
    print(i)  # [3, 6, 9, 12, 15] 출력됨