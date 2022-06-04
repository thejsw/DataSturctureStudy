# 양방향 연결 리스트
## 각 노드가 앞뒤 양방향으로 연결됨
## 단방향으로 순회할 시에 발생하는 단점 해소

class BidirectNode:
    def __init__(self, x, prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode

class DoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def insert(self, i:int, newItem):  
        if i >= 0 and i <= self.__numItems: 
            prev = self.__getNode(i - 1)   #prev는 getNode의 번호보다 1작게 선언 > 몇번째 아이템인가?
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")
    
    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)   #맨끝에 있는 아이템을 prev로 선언
        newNode = BidirectNode(newItem, prev, prev.next)
        newNode.next.prev = newNode
        prev.next = newNode
        self.__numItems += 1
    
    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1
        
        if (i >= 0 and i <= self.__numItems - 1):
            curr = self.__getNode(i)
            retitem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retitem
        else:
            return None
    
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next   #[prev] > [next] | [curr]
            self.__numItems -= 1
            return x
        else:
            return None

    def get(self, i:int):
        if self.isEmpty():
            return None
        if (i >= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            return None

    def index(self, x) -> int:
        curr = self.__head.next   #head [[dummy],[]] > head.next(0번째노드) [[][]]
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -2
    
    # 기타 작업들
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = BidirectNode('dummy', None)
        self.__numItems = 0

    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))
    
    def copy(self):
        a = LinkedListBasicPlus()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    def reverse(self) -> None:
        prev = self.__head
        curr = prev.next
        next = curr.next
        self.__head.next = prev.prev
        self.__head.prev = curr

        for i in range(self.__numItems):
            curr.next = prev
            curr.prev = next
            prev = curr;
            curr = next;
            next = next.next

    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])
    
    def __findNode(self, x):
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next
        return (None, None)

    def __getNode(self, i:int) -> ListNode:
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self):

        curr = self.__head.next
        while curr != None:
            print(curr.item, end = ' ')
            curr = curr.next
        print()
