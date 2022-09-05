# 힙
## 왼쪽부터 채워져있는 트리

# 포화이진트리
## 자식 노드를 2개씩 가지면서 꽉 채워진 트리
## 총 노드의 수가 2^k-1 (k는 높이) (4층일 경우 15개)

# 힙의 조건
## 완전이진트리
## 힘 특성
#### 최대 힙 > 모든 노드가 값을 갖고, 자식 노드 값보다 크거나 같다
#### 최소 힙 > 모든 노드가 값을 갖고, 자식 노드 값보다 작거나 같다


class heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []
     
    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)
    
    def __percolateUp(self, i:int):
        parent = (i - 1) // 2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)
    
    def deleteMax(self):
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return max
        else:
            return None
    
    def __percolateDown(self, i:int):
        child = 2 * i + 1
        right = 2 * i + 2
        if (child <= len(self.__A)-1):
            if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
                child = right
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
    
    def max(self):
        return self.__A[0]
    
    def buildHeap(self):
        for i in range((len(self.__A) - 2) // 2, -1, -1):
            self.__percolateDown(i)
    
    def isEmpty(self) -> bool:
        return len(self.__A) == 0
    
    def clear(self):
        self.__A = []
    
    def size(self) -> int:
        return len(self.__A)

    def heapPrint(self):
        print('===================')
        i = 0
        j = 1

        while (1):
            try:
                for k in range(i, j):
                    print(self.__A[k], end= " ")
                print()
                print()
        
                i = 2 * i+1
                j = 2 * i+1
            except:
                print()
                return
        # a = 2
        # ans = 1
        # for _ in range(len(self.__A)):
        #     ans *= a

        # for i in range(1, len(self.__A)):
        #     if (i==1):
        #         print(self.__A[i])
        #     else:
        #         for j in range(i):
        #             j *= 2
        #             print(self.__A[j])

        # def power(n):
        #     a = 2
        #     ans = 1
        #     return ans

        # for i in range(len(self.__A)):
        #     for j in range(i):
        #         print(self.__A[i], end = ' ')
        #     i += 1
        # print()


    # def heapPrint(self):
    #     n = len(self.__A)
        
    #     for i in range(0, n, -1):
    #         print(self.__A[i])
    #         self.__A[i], self.__A[i+1] = self.__A[i+1], self.__A[i]
    #         heap(self.__A, 1, i-1)