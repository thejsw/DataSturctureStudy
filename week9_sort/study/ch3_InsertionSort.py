# 3. 삽입 정렬

## 정렬된 리스트의 하나씩 늘리며, 늘릴 때마다 포함되는 원소를 알맞은 자리에 넣기
## 시간복잡도 Average, Worst: 세타(n*), Best: 세타(n)

def insertionSort(A):
    for i in range(1, len(A)):
        loc = i-1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = newItem