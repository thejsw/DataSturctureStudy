def mergeSort(A, p:int, r:int):  # A: 리스트, p: 리스트의 시작값, r: 리스트의 끝값
    if (p < r):
        q = (p+r) // 2  # 절반으로 나누기
        mergeSort(A, p, q)  # 전반부 mergeSort
        mergeSort(A, q+1, r)  # 후반부 mergeSort
        merge(A, p, q, r)  # 합치는 과정
    
def merge(A, p:int, q:int, r:int):
    i = p
    j = q+1
    t = 0
    tmp = [0 for i in range(len(A))]  # 임시적인 리스트 추가

    while (i <= q and j <= r):
        if (A[i] <= A[j]):
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            i += 1
    
    while (i <= q):
        tmp[t] = A[i]
        t += 1
        i += 1
    
    while (j <= r):
        tmp[t] = A[j]
        t += 1
        j += 1
        i = p
        t = 0
    
    while (i <= r):
        A[i] = tmp[t]
        t += 1
        i += 1

A = [3, 4, 5, 1, 2]
result = mergeSort(A)
print(result)