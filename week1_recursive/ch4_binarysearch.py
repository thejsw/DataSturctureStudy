# 이진탐색 알고리즘
# 시간복잡도 : O(log n)

def binary(list, x, low, high):
    if (low > high):
        return "Not Found"
    mid = (high - low) / 2
    if (list[mid] < x):
        return binary(list, x, mid+1, high)
    elif (list[mid] > x):
        return binary(list, x, low, mid-1)
    else:
        return mid


# 실행결과
list = [1, 2, 3, 4, 5]
x = 5

answer = binary(list, x, low, high)
print(answer)