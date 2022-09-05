# 색인 - 인덱싱
## 레코드 - 개체에 대한 정보
## 색인 - 레코드를 검색하기 위한 정보
## 키 - 각 레코드를 구분할 수 있는 필드


# 이진 검색 트리
## 각 노드는 킷값을 하나씩 갖고, 각 노드의 킷값은 모두 다르다.
## 최상위 레벨에 루트 노드가 있고, 최대 2개의 자식 노드를 갖는다.
## 킷값은 왼쪽 아래보다는 크고, 오른쪽 아래보다는 작다.

# 객체 구조
## item, left, right

# 검색
## 키가 x인 노드 검색
## 성공시 해당 노드 리턴, 실패 시 None 리턴 

def insert(x):
    root = insert(root, x)

def insertItem(t, x):
    if (t = None):  # t가 아예 없다면, 노드를 새로 만든다.
        r.item = x
        r.left = None
        r.right = None
        return r
    
    elif (x < t.item):  # x가 t.item보다 작다면, 왼쪽 아래에 추가
        t.left = insertItem(t.left, x)
        return t
    
    else:
        t.right = insertItem(t.right, x)  # x가 t.item보다 크다면, 오른쪽 아래에 추가
        return t
