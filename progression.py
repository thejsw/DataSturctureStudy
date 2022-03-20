n = 4

def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3
        

print(seq(n))