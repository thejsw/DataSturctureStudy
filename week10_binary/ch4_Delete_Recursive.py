# deleteSketch(r):
#     if (r이 리프 노드):
#         그냥 r을 버린다.
#     elif (r의 자식이 하나만 있음):
#         r의 부모가 r의 자식을 직접 가리키도록 한다.
#     else:
#         r의 오른쪽 서브 트리의 최소 원소 노드 s를 찾는다
#         s를 r자리로 복사하고 s를 삭제한다

def delete(t, x):
    if (t = null)
        print("item not found")
    elif (x = t.item):
        t = deleteNode(t)
        return t
    elif (x < t.item):
        t.left = delete(t.left, x)
        return t
    else:
        t.right = delete(t.right, x)
        return t
    
def deleteNode(t):
    if (t.left = None and t.right = None)
        return None
    elif (t.left = None):
        return t.right
    elif (t.right = None):
        return t.left
    else:
        (minItem, node) = deleteMinItem(t.right)
        t.item = minItem
        t.right = node
        return t
    
def deleteMinItem(t):
    if (t.left = None):
        return (t.item, t.right)
    else:
        (minItem, node) = deleteMinItem(t.left)
        t.left = node
        return (minItem, t)