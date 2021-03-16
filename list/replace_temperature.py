#화씨 온도를 섭씨 온도로 바꾸어주는 프로그램
def fahrenheit_tocelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
i = 0
while i < len(sample_temperature_list):
    sample_temperature_list[i] = fahrenheit_tocelsius(sample_temperature_list[i])
    i = i + 1

# 섭씨 온도 출력

print("섭씨 온도 리스트: " + str(sample_temperature_list))