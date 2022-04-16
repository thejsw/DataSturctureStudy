# 스택(LIFO) : 가장 먼저 들어온 것이 가장 먼저 나가는 구조 (프링글스)
## 맨 위의 원소만 접근 가능
## 삽입 시 새 원소를 맨 위에 삽입하고 top을 위로 이동
## 삭제 시 맨 위 원소를 삭제하고 top을 아래로 이동

# 구성요소
## __stack : 원소가 저장되는 리스트
## push() : 맨 위에 원소를 삽입
## pop() : 맨 위에 원소를 삭제
## top() : 맨 위에 원소를 확인
## isEmpty() : 스택이 비었는지 확인
## popAll() : 스택을 비움

class ListStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]   # __stack[len(self.__stack) -1] 과 동일
     
    def isEmpty(self) -> bool:   # bool함수 : 객체가 비어있거나, False거나, 객체의 값이 0이거나, 객체가 None인 경우 > False 반환
        return not bool(self.__stack)   # 비어있다면 True를 반환
    
    def popAll(self):
        self.__stack.clear()   # self__stack = [] 과 동일

    def printStack(self):
        print("Stack from top:", end = ' ')
        for i in range(len(self.__stack) -1, -1, -1):
            print(self.__stack[i], end = ' ')
        print()

    def parenBalance(self, s) -> bool:
        left = 0
        right = 0

        for i in range(0, len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
        if left == right:
            print('True')
        else:
            print('False')


# 실행결과
# st1 = ListStack()
# st1.push(100)
# st1.push(200)
# print("Top is {0}" .format(st1.top()))
# st1.pop()
# st1.push('Monday')
# st1.printStack()
# print("is Empty? : {0}" .format(st1.isEmpty()))

st1 = ListStack()
st1.parenBalance('(parenBalance)')
st1.printStack()