def power(n):
    a = 2
    ans = 1
    for _ in range(n):
        ans *= a
    
    return ans

pow = power(3)
print(pow)