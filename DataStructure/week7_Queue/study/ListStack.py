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