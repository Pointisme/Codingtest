def solution(scoville, K):
    answer = 0
    #섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 
    # + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    scoville.sort()
    cnt=0
    if scoville[0]>=k:
        return -1
    elif scoville[0]<K:            
        while scoville[0]<K:
            cnt+=1
            lst=[]
            new_one=0
            lst.append(scoville.pop(0))
            lst.append(scoville.pop(0))
            print(lst)
            new_one=lst[0]+lst[1]*lst[1]
            scoville.append(new_one)
            scoville.sort()

    return cnt
##########################################
#시간복잡도 충족X

lst=[6,7,10,13]
k=7
print(solution(lst,k))