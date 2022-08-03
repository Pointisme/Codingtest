from collections import defaultdict #인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정할 수 있음

def solution(id_list, report, k):
    answer=[]
    report = list(set(report))
    user = defaultdict(set)
    cnt=defaultdict(int)

    for r in report:
        a,b=r.split()
        user[a].add(b)
        cnt[b]+=1

    for i in id_list:
        result=0
        for j in user[i]:
            if cnt[j]>=k:
                result+=1
        answer.append(result)
    return answer
    
#id_list = 이용자 ID 담긴 문자열
#report = 신고당한 이용자 ID가 담긴 
#k = 정지 기준이 되는 신고 횟수
print(1)
