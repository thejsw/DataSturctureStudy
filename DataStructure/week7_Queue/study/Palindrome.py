from ListStack import *
from ListQueue import *

def isPalindrome(A) -> bool:
    s = ListStack();  # 1. 선언
    q = ListQueue();
    for i in range(len(A)):  # 2. push
        s.push(A[i]);
        q.enqueue(A[i]);
    while (not s.isEmpty()) and (s.pop() == q.dequeue()):  # 3. 비교 - Empty가 아니고, s.pop과 q.dequeue가 다를 때까지 진행
        {}
    if q.isEmpty():  # 비워졌다면 > 모두 동일
        return True
    else:
        return False
    

def main():
    print("Palindrome Check!")
    str = 'liil'
    t = isPalindrome(str)
    print(str, "isPalindrome?: ", t)

if __name__ == '__main__':
    main()