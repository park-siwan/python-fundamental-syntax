import timeit
start_time = timeit.default_timer() # 시작 시간 체크

# 강사가 나보다 45배 더 빠르다. (0.02초 소요)
for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(a * b * c)

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))