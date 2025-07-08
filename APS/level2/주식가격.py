# [문제 설명]
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# [제한사항]
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# [전략]
# 현재 위치의 주식보다 이전 위치의 주식의 가격이 높으면 -> 이전 주식 길이 확정

def solution(prices):
    answer = []
    n = len(prices)
    answer = [0] * n

    stack=[0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop() #index가 return
            answer[j] = i - j
        stack.append(i)

            # stack에 남아있는 것들은 가격 유지 혹은 오름
    while stack:
        j=stack.pop()
        answer[j]=n-1-j

    return answer

#test case
print(solution([1,2,3,2,3]))