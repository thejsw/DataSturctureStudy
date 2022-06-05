# 3. 삽입 정렬

## 정렬된 리스트의 하나씩 늘리며, 늘릴 때마다 포함되는 원소를 알맞은 자리에 넣기
## 시간복잡도 Average, Worst: 세타(n*), Best: 세타(n)

def insertionSort(A):
    for i in range(1, len(A)):
        loc = i-1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:  # 확장 과정 중 작은 원소를 발견하면,
            A[loc+1] = A[loc]  # 끝날때까지(원소가 올바른 위치에 올때까지) 자리 바꾸기
            loc -= 1  # 원소가 있어야 할 위치(location)을 하나씩 줄여주기 > 왼쪽으로 이동해야 하기 때문에
        A[loc+1] = newItem  # 자리를 다 밀고, 위치를 찾으면, 거기에 newItem 넣어주기