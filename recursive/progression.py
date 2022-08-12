n = 4

def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3

# seq(n-1)은 seq(n-2)를 호출하고, seq(n-3)을 호출하고, seq(1)일 때까지 호출한다.
# seq(1)은 1 (초항이다)로 리턴되고, seq(2)에서는 seq(1) + 3이 되어, 4가 리턴된다.
# 이러한 방식으로 seq(n)까지 진행된다.

print(seq(n))