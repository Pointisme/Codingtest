import heapq
def solution(scoville, K):
    answer = 0
    #섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 
    # + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    heapq.heapify(scoville)
    while scoville[0]<k:
        try:
            mix=heapq.heappop(scoville)+heapq.heappop(scoville)*2
            heapq.heappush(scoville,mix)
        except IndexError:
            return -1
        answer+=1

    return answer
##########################################
#시간복잡도 충족X

lst=[1,2,3,9,10,12]
k=7
print(solution(lst,k))