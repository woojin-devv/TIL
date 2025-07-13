# [문제 설명]
# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# [제한 사항]
# n은 1이상, 50000000000000 이하인 양의 정수입니다.

# Try 1
import math as m

# def solution(n):
#     print(int(m.sqrt(n) ** 2))
#     if int(m.sqrt(n) ** 2) == n:
#         return int((m.sqrt(n)+1) ** 2)
#     return -1

# sqrt() 함수 사용할 경우 소수점 8번째 자리수 까지 반환


#Try 2
import math

def solution(n):
    root = int(math.sqrt(n))
    if root * root == n:
        return (root + 1) ** 2
    return -1
print(solution(121))
print(solution(9999))