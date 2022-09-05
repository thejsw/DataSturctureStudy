def balanceAVL(t, type):
    switch(type):
        case LL: 
            우회전(t)
        case LR: 
            좌회전(t.left)
            balanceAVL(t, LL)
        case RR:
            좌회전(t)
        case RL:
            우회전(t.right)
            balanceAVL(t, RR)

def 좌회전(t):
    Rchild = t.right
    RLChild = Rchild.left
    RChild.left = t
    t.right = RLChild
    RChild.height = max(RChild.right.height, RChild.left.height) + 1
    t.height = max(t.right.height, t.left.height) + 1
    

def 우회전(t):
    Lchild = t.left
    LRChild = Lchild.right
    LRChild.left = t
    t.left = LRChild
    LChild.height = max(LChild.right.height, LChild.left.height) + 1
    t.height = max(t.right.height, t.left.height) + 1
    

