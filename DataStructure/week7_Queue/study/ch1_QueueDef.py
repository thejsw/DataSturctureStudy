# Queue

# 가장 먼저 들어온 것이 가장 먼저 나가는 구조
# FIFO (First in First out)

# 맨 앞에 있는 원소를 front (가장 먼저 삽입된 원소)
# 맨 뒤에 있는 원소를 tail (가장 마지막에 삽입된 원소)
# 원소를 삭제할 시 front를 삭제함




# 주요 구성요소
### __queue[] : 리스트

### enqueue(item) : 큐의 끝에 원소를 삽입 (append)
### dequeue() : 큐의 맨 앞에 있는 원소를 알려주고 삭제 (pop)

### front() :큐의 맨 앞에 있는 원소를 알려줌
### popAll() : 큐를 깨끗이 청소
### isEmpty() : 큐가 비었는지 알려줌



