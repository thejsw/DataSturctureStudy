# for 반복문
for i in [0, 1, 2]:
    print("hi", i)

for i in range(0, 5):
    print("bye", i)


for i in range(10, 4, -2):   #10부터 4까지 -2만큼 반복 // 4는 포함 x
    print(i, end = ' ')


# 불변 타입과 가변 타입
## 불변 타입 >> 원래의 값이 저장된 곳에서 값을 변경하지 않고, 새로운 값을 새로운 공간에 저장함
### ex) a = 3, a += 1, 둘의 주소가 다름
### 불변 타입 - 숫자, 문자열, 튜플
### 가변 타입 - 리스트, 집합, 딕셔너리


# 리스트, 튜플, 딕셔너리, 집합
## 리스트 - 값 변경 O, 중복 O
a = [1, 3, 5, 7]
## 튜플 - 값 변경 X
t = (1, 3, 5, 7)
## 딕셔너리 - 키와 밸류값으로 활용, 키 중복 X
d = {'one':10, 'two':20, 'thr':30}
d['thr'] = 333
d['fou'] = 444
for i in d:
    print(i, ':', d[i], end = ' ')
## 집합 - 중복 X, 순서 X


# 복사호출, 참조호출
## 파라미터가 불변타입(숫자,문자열,튜플) -> 복사호출, 가변타입(리스트,딕셔너리) -> 참조호출
### 혼용된 경우 타입에 따라 선택함 -> 할당호출