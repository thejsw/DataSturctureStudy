# 리스트에는 배열리스트와 연결리스트가 있음

# 리스트 내장 메소드 함수 종류
a = []
a.insert(0, 1) #0번째에1추가
a.append(1) #마지막에1추가 > 통째로 집어넣는 느낌
a.extend(1) #마지막에1추가 > 요소 하나하나 넣는 느낌
a.copy() #복사

a.pop(0) #0번째삭제
a.remove(1) #1삭제
a.clear() #비워내기

a.index(1) #1의번호
a.count(1) #1의개수
a.sort() #순서대로 정렬
a.reverse() #반대로 정렬

# 파이썬 내장 리스트의 한계
# 배열로 구현되었기 때문에
# 1. 원소 삽입/삭제 시 시프트 연산 발생 (원소 개수 만큼 연산 > 시간/공간 복잡도 업)
# 2. 공간의 크기가 미리 결정, 오버플로우 발생 시 새로운 공간에 다시 할당해서 원소 이동 (또 복사해서 또 이동하고)