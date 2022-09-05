class BidirectNode:
    def __init__(self, x, prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def insert(self, i:int, newItem):  
        if (i >= 0 and i <= self.__numItems): 
            prev = self.getNode(i - 1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")
    
    def append(self, newItem):
        # for i in range(self.__numItems):
        #     if (newItem != )
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1
    
    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        if (i >= 0 and i <= self.__numItems - 1):
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retItem
        else:
            return None
    
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
            return x
        else:
            return None

    def get(self, i):
        if self.isEmpty():
            return None
        if (i >= 0 and i <= self.__numItems - 1):
            return self.getNode(i).item
        else:
            return None

    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return -12345
    
    # 기타 작업들
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def count(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt
    
    def extend(self, a):
        for element in a:
            self.append(element)
    
    def copy(self):
        a = CircularDoublyLinkedList()
        for element in self:
            a.append(element)
        return a
    
    def reverse(self):
        prev = self.__head
        curr = prev.next
        next = curr.next
        self.__head.next = prev.prev
        self.__head.prev = curr
        for i in range(self.__numItems):
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
            next = next.next
        
    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)
    
    def __findNode(self, x):
        curr = self.__head.next
        while curr != self.__head:
            if curr.item == x:
                return curr
            else:
                curr = curr.next
        return None

    def getNode(self, i:int):
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self):
        for element in self:
            print(element, end = ' ')
        print()

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)

class CircularDoublyLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item