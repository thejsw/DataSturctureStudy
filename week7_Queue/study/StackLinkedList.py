from LinkedListBasic import *

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, newItem):
        self.__list.insert(0, newItem)
    
    def pop(self):
        self.__list.pop(0)
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.get(0)

    def isEmpty(self) -> bool:
        return self.__list.isEmpty()
    
    def popAll(self):
        self.__list.clear()

    def printStack(self):
        print("Stack from top:", end = ' ')
        for i in range(self.__list.size()):
            print(self.__list.get(i), end = ' ')
        print()


# 실행결과
st1 = LinkedStack()
st1.push(100)
st1.push(200)
print("Top is {0}" .format(st1.top()))
st1.pop()
st1.push('Monday')
st1.printStack()
print("is Empty? : {0}" .format(st1.isEmpty()))
