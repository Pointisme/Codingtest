def solution(numbers):
    answer=45
    for i in numbers:
        answer-=i
    return answer

n=[5,8,4,0,6,7,9]
print(solution(n))