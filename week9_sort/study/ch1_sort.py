## 시간복잡도는 세타(nlogn)과 O(n*) 사이
## 특수한 성질을 만족하는 경우 세타(n)도 가능

## 1. 선택 정렬 (Selection Sort)
#### 가장 큰 수를 찾고, 오른쪽으로 보냄

def selectionSort(A):
    for last in range(len(A)-1, 0, -1):  # 끝에서부터 처음으로 오면서 last을 바꿔감 > 한 칸씩 줄어듦
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]    # 끝 칸과 라스트 값이 있는 칸을 바꾸기

def theLargest(A, last:int) -> int:
    largest = 0
    for i in range(last+1):   # 0부터 last까지 순회
        if A[i] > A[largest]: # 순회하는 대상이 largest보다 크면
            largest = i       # largest 변경
    return largest

A = [3, 4, 5, 1, 2]
result = selectionSort(A)
print(result)