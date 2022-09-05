
# 가변 파라미터
## 파라미터의 개수가 경우에 따라 달라질 경우에 사용, 튜플로 전달
def pop(self,*args):

    if len(args) != 0:  # argument가 전달되었을 경우
        i = args[0]   # i에 argument 튜플 그 자체를 전달 // ex) argument가 name, age, address 일 경우 (name, age, address)로 전달됨
    
    if len(args) == 0 or i == -1:   # 인자가 없거나, -1이 전달된 경우
        i = self.__numItems - 1   #  맨 끝 원소를 삭제