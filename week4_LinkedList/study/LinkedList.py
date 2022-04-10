### 연결리스트의 객체 구조
# 동적 공간할당 방식으로 공간 효율성이 좋음 (그때그때 공간을 만들어줌 > 미리 공간을 마련해놓을 필요도, 불필요한 복사나 이동이 없음)


### 연결리스트의 구성
# __head : 첫번째 노드 > 내부변수
# __numItems : 연결 리스트에 들어 있는 원소의 총 개수 > 내부변수, 원소의 총 개수를 확인하고 싶을 때마다 매번 순회하면서 확인하면, 시간이 너무 오래 걸림 > 이를 해결하기 위해 탄생
# 파이썬 리스트 내장 함수 : insert, append 등
a = []
a.get(0) #0번째 원소를 알려줌
a.size() #총 원소 개수를 알려줌
