def BFS(G, s): # Graph, start
    for each v in V:
        print(v)
    print(s)
    enqueue(Q, s) # Queue
    while(Q != 0):
        u = dequeue(Q)
        for each v in u.adj:
            if (v.visitied == No):
                v.visitied = YES
                enqueue(Q, v)


# 1 > 2 3 > 4 5 6 > 7 8 9 10