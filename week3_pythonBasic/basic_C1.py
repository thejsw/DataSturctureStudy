# 인자 없는 함수
def greet():
    print("반갑습니다.\n")

greet()

# 인자 있는 함수
def great(name):
    print(name, "반갑습니다.\n")

great("John")

# 값을 반환 하는 함수
def plus(num1, num2):
    num3 = num1 + num2
    return num3

print(plus(1, 2))

# 값을 입력받기
old = input("How old are you?: ")
print(old)

# int 자료형과 float 자료형
data1 = 4
data2 = 3.3
print(type(data1), type(data2))
print(data1 / data2, data1 // data2)
data1 = float(data1)
data2 = int(data2)
print(data1, data2)