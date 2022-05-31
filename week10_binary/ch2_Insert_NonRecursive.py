insert(x):
    r.item <- x;
    r.left <- null;
    r.right <- null;

insertItem(t, x):
    if (root = null):
        root <- r
    
    else:
        t <- root
        while (t != null):
            parent <- t
            
            if (x < t.item):
                t <- t.left
            else:
                t <- t.right
            
            if (x < parent.item):
                parent.left <- r
            else:
                parent.right <- r
