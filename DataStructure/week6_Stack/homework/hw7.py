from StackLinkedList import *

# def fact(n):
#     while n>0:
#         # self.__stack.append(n)
#         n -= 1
#     result = 1
#     while stack:
#         # result *= stack.pop()
#     # return result

# print(fact(5))

class factorial:
    def __init__(self):
        self.__stack = LinkedStack()
    
    def fact(self, n):
        idx = s.find('$')

        while n>0:
            self.__stack.push(n)
            n-=1
        result = 1

        for i in range(n):
            result *= self.__stack.pop()

        return result

if __name__ == "__main__":
    f = factorial()
    값 = f.fact(5)
    print(값)