# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

#n은 0이상 3000이하인 정수입니다.

def solution(n):
    answer = 0
    
    for i in range(1,len(str(n))):
        answer += n % (10 ** i)
        # print(i, answer)
        answer += n // (10 ** i)
        # print(i, answer)

    return answer

# 테스트
print(solution(12))