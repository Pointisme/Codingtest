from heapq import *
def solution(scoville, K):
    cnt=0
    heapify(scoville)
    while scoville[0]<K and len(scoville)>1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville,num1+num2*2)
        cnt+=1
    return cnt if scoville[0]>=K else -1

##########################################
#시간복잡도 충족X

lst=[1,2,3,9,10,12]
k=7
print(solution(lst,k))