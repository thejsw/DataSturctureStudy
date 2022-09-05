def Prim(G, r):
    S = {r}
    r.cost = 0

    for each u in V-{r}:
        u.cost = w
    
    while (S != V):
        u = deleteMin(V-S) # 제일 작은 원소 선택
        S = S U {u} # 방문한 원소 S에 추가

        for each v in u.adj:
            if (v in V-S and w < v.cost):
                v.cost = w
                v.tree = u

def deleteMin(Q):
    # 집합 Q에서 u.cost 값이 가장 작은 정점 u를 삭제하면서 리턴한다. 