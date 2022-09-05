# 클래스
## 다양한 형태의 함수를 저장하기 위한 방법
class Member:
  counter = 0   # 클래스 변수 > 클래스 전체 사용 가능

  def __init__(self, name, age, address):   # 생성자
    self.name = name
    self.age = age
    self.address = address
    # self.__gender = gender    # 내부 변수 > 밖에서 수정이 불가능
  
  def info(self):   # 메소드
    print('저의 이름은 {0}이고, 나이는 {1}, 사는곳은 {2}입니다.' .format(self.name, self.age, self.address))
  
introduce = Member('jo', 21, 'korea')   # 클래스 Member의 인스턴스 introduce 생성
introduce.info()    # 인스턴스 introduce의 메소드 info 호출


  # 클래스 iterator 순회
  # https://wikidocs.net/134909
import collections

class NewRange:
    def __init__(self, start, end):
      self.start = 0
      self.end = 0
    
    def __iter__(self):
      return self
    
    def __next__(self):
      if self.start < self.end:
        value = self.start
        self.start += 1
        print("hey")
        return value
      else:
        raise StopIteration
    
num_list = NewRange(11, 14)
for n in num_list:
  print(n, end = ' ')
  

# __name__ == "__main__"
## python interpreter에서 직접 실행했을 경우에만 코드를 사용하라는 의미


# 패키지와 모듈
## from 모듈이름 import 클래스이름
### ex) math.py 파일 내에 class add, class divdide 등 여러 가지의 클래스가 있을 경우, from math import *을 하면, math.py 내의 class 모두 호출 가능
