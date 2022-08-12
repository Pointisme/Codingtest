def solution(n, m):
    num=2
    answer = []
    least=1
    big=0
    while num<=n and num<=m:
        if n%num==0 and m%num==0:
           least*=num
           n/=num
           m/=num
        else:
            num+=1
    big=int(least*n*m)
    answer.append(least)
    answer.append(big)
         
    return answer

print(solution(9,18))