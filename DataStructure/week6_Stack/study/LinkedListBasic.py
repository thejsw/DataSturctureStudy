class ListNode:
	def __init__(self, newItem, nextNode:'ListNode'):
		self.item = newItem
		self.next = nextNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)   #변수선언 [['dummy'],[]] 경우의 수 분기할 필요 x, 예외처리 x, 맨처음부터 더미노드가 있는 구조체로 구성// ListNode는 [[item],[next]]로 이루어진 구조체
        self.__numItems = 0   #변수선언 개수세기
    
    def insert(self, i:int, newItem):   #i의 자료형을 int로 선언
        if i >= 0 and i <= self.__numItems: #범위조절 (numItems는 원소의 개수, 원소의 개수를 넘어가지 않게끔)
            prev = self.__getNode(i - 1)   #prev는 getNode의 번호보다 1작게 선언 > 몇번째 아이템인가?
            newNode = ListNode(newItem, prev.next)   #[1] [new] > [2]  // newItem을 prev.next로 주소를 넘겨서 연결시킴
            prev.next = newNode   #[1] > [new] > [2]  // 원래노드를 새로운 노드에 연결시킴 : prev.next의 값을 새로운 노드로 변경
            self.__numItems += 1   #실행할때마다 numItems 숫자 증가
        else:
            print("index", i, ": out of bound in insert()")
    
    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)   #맨끝에 있는 아이템을 prev로 선언
        newNode = ListNode(newItem, prev.next)   
        prev.next = newNode
        self.__numItems += 1
    
    def pop(self, i:int):
        if (i >= 0 and i <= self.__numItems - 1):   #유효한 범위내에
            prev = self.__getNode(i - 1)   #i-1번째 노드를 찾고
            curr = prev.next   #i번째 노드를 curr로 연결  //  [prev] > [curr-삭제대상] > [next]
            prev.next = curr.next   #prev.next를 curr.next로 연결  //  [prev] > [next] | [curr:연결이 끊긴 상황]
            retItem = curr.item   #curr.item을 리턴하기 위한 목적
            self.__numItems -= 1
            return retItem
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
        self.__head = ListNode('dummy', None)
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
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))

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
    
    
    