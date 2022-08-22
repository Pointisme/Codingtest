def solution(N, stages):
    answer = []
    num=dict()
    remain_num=len(stages)
    for i in range(1,N+1):
        cnt=0
        for j in stages:
            if j==i:
                cnt+=1
        num[i]=cnt/remain_num
        remain_num-=cnt


   
    return  sorted(num, key = lambda item: item[1], reverse = True)



print(solution(5,[2,1,2,6,2,4,3,3]))