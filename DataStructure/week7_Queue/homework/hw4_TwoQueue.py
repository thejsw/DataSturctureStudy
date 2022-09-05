# class Stack:
#     def __init__(self):
#         self.items = []
#         self.max = 3

#     def push(self, item):
#         self.items.append(item)
    
#     def pop(self):
#         return self.items.pop()
    
#     def print_stack(self):
#         print(self.items)
    
#     def is_empty(self):
#         return self.items == []
    

# class StacktoQueue:
#     def __init__(self):
#         self.st1 = Stack()
#         self.st2 = Stack()
    
#     def enqueue(self, item):
#         self.st1.push(item)
    
#     def dequeue(self):
#         if self.st2.is_empty():
#             while self.st1.is_empty() is False:
#                 self.st2.push(self.st1.pop())
        
#         return self.st2.pop()

# if __name__ == "__main__":
#     st = StacktoQueue()
#     st.enqueue(1)
#     st.enqueue(2)
#     st.enqueue(3)
#     print(st.dequeue())
#     print(st.dequeue())
#     print(st.dequeue())

from LinkedListBasic import *

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, newItem):
        self.__list.insert(0, newItem)
    
    def pop(self):
        return self.__list.pop(-1)
    
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


class TwoStackQueue:
    def __init__(self):
        self.__st1 = LinkedStack()   # 첫번째 리스트 생성
        self.__st2 = LinkedStack()   # 두번째 리스트 생성

    def __move_element__(self, st1, st2):
        while not st1.isEmpty():   # 첫번째 리스트가 비어있지 않다면,
            st2.push(st1.pop())   # 첫번째 리스트에서 마지막 원소를 빼서 두번째 리스트에 추가

    def enqueue(self, x):
        self.__st1.push(x)   # 첫번째 리스트에 원소 추가

    def dequeue(self):
        if self.__st2.isEmpty():
            self.__move_element__(self.__st1, self.__st2)   # __move_element__ 실행 ()
        else:
            return 0
        
        return self.__st2.pop()


sq = TwoStackQueue()
sq.enqueue(1)
sq.enqueue(2)
sq.enqueue(3)

print(sq.dequeue())
print(sq.dequeue())
print(sq.dequeue())