# 리스트형 데이터
list1 = [1, 2, 3, 4, 5]
data1 = list1[0]
data5 = list1[-1]
print(data1, data5)

# 리스트 슬라이싱
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = list2[3:6] #3부터5까지
list4 = list2[0:7:2] #0부터 6까지 2개식
print(list3, list4)

# 리스트와 함수들
st = [1, 3, 5, 7 ,9]
print(len(st))
print(min(st))
print(max(st))

st.remove(9) #9를 찾아서 지운다
st.append(8) #리스트 끝에 8을 추가한다
st.insert(3, 7) #st[3]에 6을 추가한다
print(st, st.count(7)) #st에서 7의 개수를 반환한다

# 문자열과 함수들
str = "Yoon Sung Woo" #원본 보존
low = str.lower() #소문자
up = str.upper() #대문자
re = str.replace('u', 'eo') #u를 eo로 교체
spl = str.split() #공백을 기준으로 나눠서 리스트로 변환
print(low, up)
print(re, spl)

print(str.count('o')) #문자열 속 o의 개수
print(str.find('W')) #문자열 속 w의 순번

# 이스케이프 문자 : \n, \t, \', \" 등

# 튜플