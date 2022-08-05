a=15
b=1
cnt=0
while a!=1:
    if a%b==0:
        a=a/b
        b+=1
        cnt+=1
    else:b+=1
print(cnt)