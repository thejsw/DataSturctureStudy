insert(x):
    root <- insert(root, x)

insertItem(t, x):
    if (t = null):
        r.item <- x;
        r.left <- null;
        r.right <- null
        return r
    
    elif (x < t.item):
        t.left <- insertItem(t.left, x)
        return t
    
    else:
        t.right <- insertItem(t.right, x)
        return t
