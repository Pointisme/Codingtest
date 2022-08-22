def solution(nums):
    lst=[]
    for i in nums:
        if i not in lst:
            if len(lst)>=len(nums)/2:
                return len(lst)
            else:lst.append(i)
        else: continue
    answer = len(lst)
    return answer
n=[3,3,3,2,2,4]
print(solution(n))