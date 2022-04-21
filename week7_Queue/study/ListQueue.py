class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, item):
        self.__queue.append(item)
    
    def dequeue(self):
        self.__queue.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]
    
    def isEmpty(self) -> bool:
        return (len(self.__queue) == 0)
    
    def dequeueA(self):
        self.__queue.clear()
    
    def printQueue(self):
        print("Queue from front:", end = ' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end = ' ')
        print()


# 실행결과
# q1 = ListQueue()
# q1.enqueue("Mon")
# q1.enqueue("Tue")
# q1.enqueue("Wed")
# q1.dequeue()
# q1.printQueue()