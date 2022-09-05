# deleteSketch(r):
#     if (r이 리프 노드):
#         그냥 r을 버린다.
#     elif (r의 자식이 하나만 있음):
#         r의 부모가 r의 자식을 직접 가리키도록 한다.
#     else:
#         r의 오른쪽 서브 트리의 최소 원소 노드 s를 찾는다
#         s를 r자리로 복사하고 s를 삭제한다

def delete(r, p):
    if (r = root):
        root = deleteNode(root)
    elif (r = p.left):
        p.left = deleteNode(r)
    elif (r = p.right):
        p.right = deleteNode(r)

def deleteNode(r):
    if (r.left = r.right = null):
        return null
    elif (r.left = null and r.right != null):
        return r.right
    elif (r.left != null and r.right = null):
        return r.left
    else:
        s = r.right

        while(s.left != null):
            parent = s
            s = s.left
        
        r.item = s.item

        if (s = r.right):
            r.right = s.right
        else:
            parent.left = s.right
            return r