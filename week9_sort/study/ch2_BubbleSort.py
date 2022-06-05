# 2. 버블 정렬

## 이웃한 두 수를 비교하여 제일 큰 원소를 오른쪽 끝으로 보냄
## 시간복잡도: 세타(n*)

A = [3, 4, 2, 1, 5]

def BubbleSort(A):
    for numElements in (len(A), 0, -1):
        for i in range(numElements-1):
            if A[i] > A[i+1]: # 더 클 경우 이웃한 두 수의 자리를 바꾸는 방식
                A[i], A[i+1] = A[i+1], A[i]
    return A

result = BubbleSort(A)
print(result)