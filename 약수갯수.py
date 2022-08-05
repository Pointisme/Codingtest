def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        b=1
        cnt=0
        while i>=b:
            if i%b==0:
                cnt+=1
                b+=1
            else:
                b+=1
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
    return answer



print(solution(13,17))


#제곱근이 정수이면 약수의 갯수는 홀수개