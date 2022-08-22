def solution(s):
    answer=[]
    temp=''
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2:
                temp+=s[i][j].lower()
            else:
                temp+=s[i][j].upper()
        answer.append(temp)
        temp=''
    return (" ").join(answer)


print(solution("try hello world"))