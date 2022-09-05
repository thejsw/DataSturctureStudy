from unicodedata import digit
from stack import *

# def evaluate(str):
#     st = ListStack()          # 1. 선언 - 리스트
#     digitPreviosuly = False   # 1. 선언 - 불린형 변수 선언 (이전에 숫자가 나왔는가?)
#     for i in range(len(str)): # 2. push
#         ch = str[i]   # 문자열 형태로 하나씩 ch에 저장
#         if ch.isdigit():   # 2-1. .isdigit() - 숫자인가 아닌가? - 숫자일 때
#             if digitPreviosuly:  # digitPreviosuly가 True일 때
#                 tmp = st.pop()   # tmp에 이전 숫자 저장
#                 tmp = 10 * tmp + (ord(ch) - ord('0'))  # 이전 숫자의 자릿수를 올리고 / 아스키코드 변환을 통해 1의자리 숫자 형태로 저장
#                 st.push(tmp)     # tmp를 push함
#             else:                # 이전이 숫자가 아닐때
#                 st.push(ord(ch) - ord('0'))   # 그냥 아스키코드 변환만 하기
#                 digitPreviosuly = True        # 다음에 숫자가 나올 것을 대비해, True로 바꾸기
#         elif isOperator(ch):          # 2.2 isOperatior - 연산자
#             st.push(operation(st.pop(), st.pop(), ch))   # 가장 최근에 넣은 숫자, 두번째로 최근에 넣은 숫자, 현재(연산자)를 pop하여 넘김
#             digitPreviosuly = False   # 연산자 - 숫자가 아니므로 digitPreviously를 False로 바꿈
#         else:   
#             digitPreviosuly = False   # 공백 - 숫자가 아니므로 digitPreviously를 False로 바꿈
#     return st.pop()

# def isOperator(ch) -> bool:   # 3. isOperator
#     return (ch == '+' or ch == '-' or ch == '*' or ch == '/')   # ch가 연산자일 때 True 반환

# def operation(opr2:int, opr1:int, ch) -> int:   # 4. operation, 빼기와 나누기를 고려해 opr2와 opr1의 위치를 바꿈
#     return {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2} [ch]

# def main():
#     postfix = "700 3 47 + 6 * - 4 /"
#     print("Input string: ", postfix)
#     answer = evaluate(postfix)
#     print("Answer: ", answer)
#     print(ord('0'), ord('9'))

# if __name__ =="__main__":
#     main()


def evaluate(str):
    st = ListStack()
    digitPreviosuly = False
    for i in range(len(str)):
        ch = str[i]
        if ch.isdigit():
            if digitPreviosuly:
                tmp = st.pop()
                tmp = 10 * tmp + (ord(ch) - ord('0'))
                st.push(tmp)
            else:
                st.push(ord(ch) - ord('0'))
                digitPreviosuly = True
        elif isOperator(ch):
            st.push(operation(st.pop(), st.pop(), ch))
            digitPreviosuly = False
        else:
            digitPreviosuly = False
    return st.pop()

def isOperator(ch) -> bool:
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(num2:int, num1:int, ch) -> int:
    return {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 // num2} [ch]

def main():
    postfix = "700 3 47 + 6 * - 4 /"
    print("Input string: ", postfix)
    answer = evaluate(postfix)
    print("Answer: ", answer)
    print(ord('0'), ord('9'))

if __name__ =="__main__":
    main()