#  사전(dictionary)은 순서가 없는 key-value 쌍의 집합이다.

# 정수인 key
dict1 = {}
print(type(dict1))

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)
print(dict1[5])
print(dict1[2])

# 정수가 아닌 key
family = {}
family['mom'] = 'na young'
family['dad'] = 'ghwang hee'
family['son'] = 'siwan'
family['sister'] = 'so won'
print(family['son'])

# dictionary key 모두 받아오기
print(family.keys())

# 원하는 key 가 있는지 확인하는 방법
print('son' in family.keys())
print('uncle' in family.keys())

# dictionary 를 list 로 형변환 하는 방법
family_keys = list(family.keys())
print(family_keys)
print(type(family_keys))

# dictionary 의 value 모두 받아오기
print(family.values())

# dictionary 에 원하는 value 가 있는지 확인하기
print('siwan' in family.values())
print('jung suk' in family.values())

# dictionary 에 value 를 list로 형변환
family_values = list(family.values())
print(family_values)
print(type(family_values))