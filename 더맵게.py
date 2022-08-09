import heapq
def solution(scoville, K):
    answer = 0
    #섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 
    # + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    heap=[]
    for i in scoville:
        heapq.heappush(heap,i)
    cnt=0
    while heap[0]<k:
        try:
            heapq.heappush(heap,heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
        cnt+=1

    return cnt
##########################################
#시간복잡도 충족X

lst=[1,2,3,9,10,12]
k=7
print(solution(lst,k))