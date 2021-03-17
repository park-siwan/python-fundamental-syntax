# 피타고라스의 정리
def pythagorean_number(a, b, c):
    if (a ** 2) + (b ** 2) == (c ** 2):
        print("(%d, %d, %d) = %d " % (a, b, c, a + b + c))
        print(a * b * c)

# a < b < c 일때 a + b + c = 1000 만족하는 수
for a in range(3, 1000):
    for b in range(4, 1000):
        for c in range(5, 1000):
            if (a < b < c) and (a + b + c == 1000):
                pythagorean_number(a, b, c)
