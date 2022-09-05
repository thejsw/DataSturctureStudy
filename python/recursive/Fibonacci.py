n = 5

def fib(n):
    if (n==1 or n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 등차수열 재귀함수와 흡사한데, n-1, n-2 작업을 통해 n이 1,2일 때까지 돌아간다.
# n이 1이거나 2면, 1을 리턴하고, 3부터는 fib(1)+fib(2)를 리턴한다.
print(fib(n))
