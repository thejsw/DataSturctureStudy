def hanoi(n, A, B, C):
    if n == 1:
        print(A, '->', B)
        return
    
    hanoi(n-1, A, C, B)
    print(A, '->', B)
    hanoi(n-1, C, B, A)

print(hanoi(3, 1, 3, 2))