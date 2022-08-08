def solution(progresses, speeds):
    take=[]
    for i,j in zip(progresses,speeds):
        cnt=0
        remain=0
        remain=100-i
        if remain%j==0:
            cnt=remain/j
        else:
            cnt=remain/j+1
        take.append(round(cnt))
    answer=[]
    cnt=1
    for i in range(len(take)):
        try:
            if take[i] < take[i + 1]:
                print(take[i], take[i+1], count)
                answer.append(count)
                count = 1
            else:
                print(take[i], take[i+1], count)
                take[i + 1] = take[i]
                count += 1
                print(take)
        except IndexError:
            answer.append(count)

    
    return answer
    
lst1=[93,30,55]
lst2=[1,30,5]
print(solution(lst1,lst2))