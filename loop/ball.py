# i = 1
# ball = 60.0
# while i <= 10:
#     print(i, ball)
#     ball = ball * 0.6
#     ball = round(ball, 4)
#     i += 1

height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i = i + 1
