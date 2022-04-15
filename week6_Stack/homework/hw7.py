# factorial

s = 'abcd$dcba'

def fact(n):
    stack = []
    while n>0:
        stack.append(n)
        n -= 1
    result = 1
    while stack:
        result *= stack.pop()
    return result

print(fact(5))