# [문제 설명]
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 
# solution 함수를 완성해주세요.

# [제한사항]
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

# 해결전략
# 1. 차집합을 이용하여 0부터 9까지의 숫자 중 numbers에 없는 숫자를 찾는다.
# 2. 찾은 숫자들을 모두 더하여 결과를 반환한다.

def solution(numbers):
    answer = 0
    
    s1 = {0, 1,2,3,4,5,6,7,8,9}
    numbers = set(numbers)
    s3 = s1 - numbers
    
    for number in s3:
        print(number)
        answer += number
    return answer

# 테스트 케이스
print(solution([1,2,3,4,6,7,8,0])) # 출력: 14
print(solution([5,8,4,0,6,7,9])) 