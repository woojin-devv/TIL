# [문제 설명]
# 정수 배열 numbers가 주어집니다. 
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

#[전략]
# 1. 두 수를 뽑아 더함
# 2. 더한 값을 배열에 저장
# 3. 오름차순으로 정렬 -> 중복값 제거 
# 4. return

def solution(numbers):
    ret = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ret.append(numbers[i]+numbers[j])
        ret = sorted(set(ret))
    return ret

#test
print(solution([2,1,3,4,1])) #기댓값 [2, 3, 4, 5, 6, 7]
print(solution([5,0,2,7])) #기댓값 [2, 5, 7, 9, 12]