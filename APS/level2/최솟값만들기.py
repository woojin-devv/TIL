# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# [문제 설명]
# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

# 예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

# A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
# A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
# A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
# 즉, 이 경우가 최소가 되므로 29를 return 합니다.

# 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

# [제한사항]
# 배열 A, B의 크기 : 1,000 이하의 자연수
# 배열 A, B의 원소의 크기 : 1,000 이하의 자연수

# Try 1 : 시간 초과..
# 문제점 min(), max() 매 반복 계산 -> 각각 O(N)
# range(len(A)) 매 반복 계산 -> O(N)
# 따라서 시간복잡도 O(N^2) -> 시간 초과

# def solution(A,B):
#     answer =0
    
#     #1. A에서 최솟값, B에서 최댓값 뽑기 / A에서 최댓값, B에서 최솟값뽑기. 
#     #2. (1)의 내용에서 크기 비교
#     #3. 크기가 작은 것을 answer에 더한 다음 배열에서 더한 값 제외 
#     #4. 배열이 0이 될 때까지 반복 (A와 B의 배열이 같으므로 반복횟수 len(A) or len(B))
    
#     for num in range(len(A)):
#         if min(A) * max(B) >= max(A) * min(B):
#             answer += max(A) * min(B)
#             A.remove(max(A))
#             B.remove(min(B))
#         else: 
#             answer += min(A) * max(B)
#             A.remove(min(A))
#             B.remove(max(B))
#     return answer

# Try 2 : 시간 초과 해결
# 문제점 : min(), max() 매 반복 계산 -> 각각 O(N)
# 해결 : A, B를 정렬하여 오름차순, 내림차순
# 시간복잡도 O(NlogN) -> 시간 초과 해결

def solution(A, B):
    A.sort()        # 오름차순
    B.sort(reverse=True)  # 내림차순

    return sum(a * b for a, b in zip(A, B))