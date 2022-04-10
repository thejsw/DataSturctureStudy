# 원형 연결 리스트
## __tail을 통해 접근 > __head 불필요


# 연결리스트와의 복잡도 비교 - 맨앞 삽입/삭제
## 연결리스트 -- 빅오(1) // 원형 연결리스트 -- 빅세타(1)


# 가변 파라미터
## 파라미터의 개수가 경우에 따라 달라질 경우에 사용, 튜플로 전달
def pop(self,*args):

    if len(args) != 0:  # argument가 전달되었을 경우
        i = args[0]   # i에 argument 튜플 그 자체를 전달 // ex) argument가 name, age, address 일 경우 (name, age, address)로 전달됨
    
    if len(args) == 0 or i == -1:  
        i = self.__numItems - 1
    
    if (i >= 0 and i <= self.__numItems - 1):   #유효한 범위내에
            prev = self.__getNode(i - 1)   #i-1번째 노드를 찾고
            curr = prev.next   #i번째 노드를 curr로 연결  //  [prev] > [curr-삭제대상] > [next]
            prev.next = curr.next   #prev.next를 curr.next로 연결  //  [prev] > [next] | [curr:연결이 끊긴 상황]
            retItem = curr.item   #curr.item을 리턴하기 위한 목적
            self.__numItems -= 1
            return retItem
        else:
            return None