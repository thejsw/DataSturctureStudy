from stack import *

def reverse(str):
    st = ListStack()   # 클래스 ListStack() = []
    for i in range(len(str)):   # 문자 하나씩 push
        st.push(str[i])
    out = ""    # 빈 문자열 생성
    while not st.isEmpty():   # 비어있지 않을 때까지
        out += st.pop()   # 빈 문자열에 st에서 제거한 문자를 하나씩 추가
    return out   # reverse된 문자열 반환

def main():
    input = "Test Seq 12345"
    answer = reverse(input)
    print("Input string: {0}" .format(input))
    print("Reversed string: {0}" .format(answer))

if __name__ == "__main__":
    main()