# 5766

N,M = map(int,input().split())

while N != 0 and M != 0:
    
    playerDic = {}
    
    
    for i in range(N):
        player = map(int,input().split())
        for num in player:
            if num not in playerDic:
                playerDic[num] = 1
            else:
                playerDic[num] += 1
    
    lst =sorted(playerDic.items(),key=lambda x: x[1], reverse=True)
    maxV = lst[0][1]
    
    second = 0 # 2등 점수 찾기
    
    for key, value in lst:
        if value < maxV:
            second = value
            break
    
    answer = []
    for key, value in playerDic.items():
        if second == value:
            answer.append(key)
    
    answer.sort()
    print(*answer)
    
    
    
    N,M = map(int,input().split()) # 종료 0,0
        
        
