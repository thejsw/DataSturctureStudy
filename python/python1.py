
print('파이썬')
# print('파이썬')

# 자료형 > 정수, 실수, 문자형(따옴표감싸줘야함)
# 변수 >
a = 3
b = 4

a = 5
b = 6

print(a + b)

# 입력 input
# a = input()
# b = input()
# c = float(a) + int(b)
# print(c)

# 조건문: if
# 반복문: for

# 술 판매 
age = int(input('몇살이세요? '))
if (age > 19):
  {print('술 구매가 가능합니다')}
elif (age == 19):
  print('좀만 참으세요.')
else:
  print('술 구매가 안됩니다.')


while (age > 19):
  print(age)
  age-=1