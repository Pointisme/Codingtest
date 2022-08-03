#lottos = 민우의 번호
#win_nums = 당첨번호
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    zero = lottos.count(0)    # lottos 안의 0의 개수를 반환
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    return rank[zero cnt],rank[cnt]