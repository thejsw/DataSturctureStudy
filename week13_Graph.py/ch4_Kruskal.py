def Kruskal(G):
    T = 0
    # 각각 단 하나의 정점만으로 이루어진 n개의 집합을 초기화한다.
    # 모든 간선을 가중치의 크기순으로 정렬하여 배열 A에 저장한다.
    # while (T의 간선수 < n-1)
        # A에서 최소 비용 간선 u-v를 제거한다.
        # if (정점 u와 v가 다른 집합에 속함)
            # T = T U {(u-v)} < 간선 u-v를 더함
            # 정점 u와 v가 속한 두 집합을 하나로 합친다.
