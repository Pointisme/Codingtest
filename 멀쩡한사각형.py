import math
def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))


#gcd = 최대공약수
#lcm = 최소공배수
