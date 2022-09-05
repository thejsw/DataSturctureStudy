from CircularDoublyLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.__queue = CircularDoublyLinkedList()
    
    def enqueue(self, item):
        self.__queue.append(item)
    
    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        return self.__queue.get(0)
    
    def isEmpty(self) -> bool:
        return self.__queue.isEmpty()
    
    def dequeueA(self):
        self.__queue.clear()
    
    def printQueue(self):
        print("Queue from front:", end = ' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end = ' ')
        print()