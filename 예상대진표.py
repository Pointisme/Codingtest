def solution(n,a,b):
    answer = 1
    while abs(a-b) != 1:
        if a % 2 != 0:
            a+=1
            a=int(a/2)
            print("a")
            print(a)
        else: a=int(a/2)
        if b % 2 != 0:
            b+=1
            b=int(b/2)
            print("B")
            print(b)
        else : b=int(b/2)
        if a == b : break
        answer+=1
        


    return answer

print(solution(16,1,16))