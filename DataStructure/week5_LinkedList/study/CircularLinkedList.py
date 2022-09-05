# 원형 연결 리스트
## __tail을 통해 접근 > __head 불필요


# 연결리스트와의 복잡도 비교 - 맨앞 삽입/삭제
## 연결리스트 -- 빅오(1) // 원형 연결리스트 -- 빅세타(1)


class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)   # 더미 헤드
        self.iterPosition = self.__head.next   # 0번 노드
    def __next__(self):
        if self.iterPosition == self.__head:   # 순환 끝
            raise StopIteration
        else:   # 현재 원소를 리턴하면서 다음 원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item