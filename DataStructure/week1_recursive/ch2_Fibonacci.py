## 피보나치 수열
## 시간복잡도 : O(n*)

n = 5

def fib(n):
    if (n==1 or n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))