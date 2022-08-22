def solution(numbers, target):
    answer = 0
    compare=0
    for i in range(len(numbers)*2):
        
        if compare==target:
            answer+=1
        else: continue
    return answer