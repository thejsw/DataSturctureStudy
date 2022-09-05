def quicksort(A, p:int, r:int):
    if (p < r):
        q = partition(A, p, r)  # 분할
        quicksort(A, p, q-1)    # 왼쪽 부분 리스트 정렬
        quicksort(A, q+1, r)    # 오른쪽 부분 리스트 정렬

# 1구역: 기준 원소보다 작은 원소들을 정렬한 구역
# 2구역: 기준 원소보다 큰 원소들을 정렬한 구역
# 3구역: 아직 정렬되지 않은 원소들

def partition(A, p:int, r:int) -> int:
    x = A[r]  # x: 기준 원소
    i = p-1   # i: 1구역의 끝 지점, p: 2구역의 시작 지점

    for j in range(p, r): # j: 3구역의 시작 지점
        if A[j] < x:
            i += 1 # 3구역 탐색 과정에서, 기준 원소보다 작은 원소가 발견되면,
            A[i], A[j] = A[j], A[i] # 1구역의 끝지점과 해당 원소를 교환
    
    A[i+1], A[r] = A[r], A[i+1]  # 기준 원소와 i+1 원소 교환
    return i+1