# JadenCase란 모든 단어의 첫 문자가 대문자이고, 
# 그 외의 알파벳은 소문자인 문자열입니다. 
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.


#제한조건 
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.

#해결전략
#1. 공백을 기준으로 문자열을 나누어 리스트에 저장 
#2. 각 단어의 첫 글자를 대문자로 바꾸고 나머지 글자는 소문자로 바꾼다.
#3. 리스트를 다시 문자열로 합쳐서 반환한다.

##주의 
#1. split() 메서드를 사용하여 문자열을 공백 기준으로 나누면, 연속된 공백은 하나의 공백으로 처리된다.

def solution(s):
    answer = []
    _list = []
    #1. 공백을 기준으로 문자열을 나누어 리스트에 저장
    _list = s.split(" ")
    print(_list)
    #2. 각 단어의 첫 글자를 대문자로 바꾸고 나머지 글자는 소문자로 바꾼다.
    for i in range(len(_list)):
        if _list[i]:
            _list[i] = _list[i][0].upper() + _list[i][1:].lower()
    #3. 리스트를 다시 문자열로 합쳐서 반환한다.
    answer = ' '.join(_list)
    return answer

#test case1
print(solution("3people unFollowed me"))
print(solution(" for the last week "))

#[try 1] 
# def solution(s):
#     _list = []
#     #1. 공백을 기준으로 문자열을 나누어 리스트에 저장
#     _list = s.split()
#     #2. 각 단어의 첫 글자를 대문자로 바꾸고 나머지 글자는 소문자로 바꾼다.
#     for i in range(len(_list)):
#         if _list[i]:
#             _list[i] = _list[i][0].upper() + _list[i][1:].lower()
#     #3. 리스트를 다시 문자열로 합쳐서 반환한다.
#     answer = ' '.join(_list)
#     return answer