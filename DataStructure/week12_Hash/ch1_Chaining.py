## 연결리스트를 통해 해시테이블에서 삽입, 검색, 삭제 구현

from ch0_DoublyLinkedList import *

class ChainingHashTable:
    def __init__(self, n):
        self.__table = [DoublyLinkedList() for i in range(n)]
        self.__numItems = 0
    
    def __hash__(self, x:int):
        return x % len(self.__table)
    
    def insert(self, x:int):
        slot = self.__hash(x)
        self.__table[slot].insert(0, x)
        self.__numItems += 1
    
    def search(self, x:int) -> BidirectNode:
        slot = self.__hash(x)
        if self.__table[slot].isEmpty():
            return None
        else:
            head = prev = self.__table[slot].getNode(-1)  #더미 헤드부터 원하는 노드가 나올 때까지 검색
            curr = prev.next
            while curr != head:
                if curr.item == x:
                    return curr
                else:
                    prev = curr
                    curr = curr.next
        
    def delete(self, x:int):
        slot = self.__hash(x)
        success = self.__table[slot].remove(x)
        if success != None:
            self.__numItems -= 1
    
    def isEmpty(self):
        return self.__numItems == 0
    
    def clear(self):
        for i in range(len(self.__table)):
            self.__table[i] = DoublyLinkedList()
        self.__numItems = 0

            