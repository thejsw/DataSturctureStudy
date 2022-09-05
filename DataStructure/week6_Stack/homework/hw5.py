from LinkedListBasic import *

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, newItem):
        self.__list.insert(0, newItem)
    
    def pop(self):
        return self.__list.pop(0)
    
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

def parenBalance(s):
    st = LinkedStack()

    for ch in s:
        if ch == '(':
            st.push(ch)
        elif ch == ')':
            isNone = st.pop()
            if (isNone == None):
                return False

                   
    return st.isEmpty()


checker = parenBalance('(()')
print(checker)