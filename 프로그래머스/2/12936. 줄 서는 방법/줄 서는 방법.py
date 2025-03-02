import math

def solution(n, k):
    lst = [i for i in range(1,n+1)]
    stack = []
    k -= 1
    
    while lst:
        
        # 앞 자리 구하기
        a = k//math.factorial(n-1)
        stack.append(lst[a])
        del lst[a]
        
        # k 줄이기
        k =k%math.factorial(n-1)
        n-=1
    return stack