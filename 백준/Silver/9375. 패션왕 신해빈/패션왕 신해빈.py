# 9375 - 패션왕 신혜빈

# [hat : headgear , sunglasses : eyewear , turban : headgear]



def solution():
    n = int(input()) # 몇 개 있는 지
    
    clothes = {}
    
    for _ in range(n):
        name, type = input().split()
        
        if type in clothes:  ## clothes안에 타입이 있다면 1추가
            clothes[type]+=1
        else:
            clothes[type] =1
    
    result = 1
        
    for count in clothes.values():
        result *= (count+1)

    
    result -= 1 # 알몸이 되는 경우
    
    print(result)


T = int(input())

for _ in range(T):
    solution()

