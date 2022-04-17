# find 함수 구현
# $ 기준으로 split
# 나눈 왼쪽 단어 len 확인
# 왼쪽 - 0에서 시작, 1씩, len까지
# 오른쪽 - len에서 시작, -1씩, 0까지
# 계속 맞는지 확인, 아닐경우 바로 중단하고 False 리턴

from StackLinkedList import *

class sentenceChecker:
    def __init__(self):
        self.__stack = LinkedStack()
    
    def is_included(self, s):
        idx = s.find('$')

        for i in range(idx):
            self.__stack.push(s[i])
        
        for i in range(idx+1, len(s)):
            prev = self.__stack.pop()
            curr = s[i]

            if prev != curr:
                return False
        
        return self.__stack.isEmpty()

if __name__ == "__main__":
    s = 'abcde$edcba'
    checker = sentenceChecker()
    rv = checker.is_included(s)
    if rv == True:
        print("True")
    else:
        print("False")

