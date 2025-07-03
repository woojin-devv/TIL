#
# [문제 설명]
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
# (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다).
# X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. 
# X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

# 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
# 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
# (X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

# [제한사항]
# 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
# X, Y는 0으로 시작하지 않습니다.
# X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.

# 각 숫자(0~9)에 대해 등장 횟수를 센다.
# 두 수에서 등장 횟수의 최솟값만큼 짝지을 수 있다.
# 큰 숫자부터 조합해 가장 큰 수를 만든다. -> sort 재정렬 한다음에 string으로 변환하면 되지 않나??

# 1차 실행 -> 시간초과... 시간복잡도 o(n^2)됨 
# def solution(X, Y):
#     answer = []
#     digits_X= [int(d) for d in str(X)]
#     digits_Y= [int(d) for d in str(Y)]
#     used = [False] * len(digits_Y)

#     for i in range(len(digits_X)):
#         for j in range(i+1,len(digits_Y)):
#             if digits_X[i] == digits_Y[j] and not used[j]:
#                 answer.append(digits_X[i])
#                 used[j] = True 
#                 break

#     answer = sorted(answer, reverse=True)
#     result = ''.join(map(str, answer))
#     if not answer:
#         return "-1"
    
#     return "0" if result[0] == "0" else result
from collections import Counter

def solution(X, Y):
    count_X = Counter(str(X))
    count_Y = Counter(str(Y))
    
    result = []
    for digit in map(str, range(9, -1, -1)):
        if digit in count_X and digit in count_Y:
            result.append(digit * min(count_X[digit], count_Y[digit]))
    
    if not result:
        return "-1"
    
    result_str = ''.join(result)
    return "0" if result_str[0] == "0" else result_str
#test cases
print(solution(100, 2345))
print(solution(100,203045))
print(solution(100, 123450))
print(solution(12321,42531))
print(solution(5525, 1255))