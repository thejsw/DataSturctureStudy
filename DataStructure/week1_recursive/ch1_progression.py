## 초항이 1인 등차수열
## 시간복잡도 : O(n)
n = 4   # n
d = 3   # 공차

def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + d
        

func_pro = seq(n)
print(func_pro)