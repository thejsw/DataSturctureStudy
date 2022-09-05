# 배열리스트 : 정적할당(시작부터 고정된 크기의 공간 할당) -> 데이터의 양을 미리 알 경우, 데이터를 리드할 경우가 많을 때 유리
# 연결리스트 : 동적할당(원소가 들어오는 대로 공간 할당) [[데이터],[포인터]] 

# 시간복잡도 -- insert -- remove -- get
## 배열리스트 - 위치접근(1), 삽입(n) - 원소찾기(n), 삭제(n) - 빅세타(1)
## 연결리스트 - 위치접근(n), 삽입(1) - 원소찾기(n), 삭제(1) - 빅오(n)

# 복잡도 계산
## 빅오(점근적상한), 빅오메가(점근적하한), 빅세타(동일)