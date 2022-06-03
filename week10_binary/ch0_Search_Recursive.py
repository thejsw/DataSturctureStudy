def search(t, x):
    if (t = None || t.item = x):  # 만약 t가 없거나, t.item이 같을 경우,
        return t
    else if (x < t.item)  # 만약 t가 찾은 원소보다 작다면
        return search(t.left, x)  # 한 칸 왼쪽으로 내려가서 다시 찾기
    else if (x < t.item)  # 만약 t가 찾은 원소보다 크다면
        return search(t.right, x)  # 한 칸 오른쪽으로 내려가서 다시 찾기
        