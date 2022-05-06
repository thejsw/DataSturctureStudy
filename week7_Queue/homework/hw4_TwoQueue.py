class Stack:
    def __init__(self):
        self.items = []
        self.max = 3

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def print_stack(self):
        print(self.items)
    
    def is_empty(self):
        return self.items == []
    

class StacktoQueue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
    
    def enqueue(self, item):
        self.st1.push(item)
    
    def dequeue(self):
        if self.st2.is_empty():
            while self.st1.is_empty() is False:
                self.st2.push(self.st1.pop())
        
        return self.st2.pop()

if __name__ == "__main__":
    st = StacktoQueue()
    st.enqueue(1)
    st.enqueue(2)
    st.enqueue(3)
    print(st.dequeue())
    print(st.dequeue())
    print(st.dequeue())