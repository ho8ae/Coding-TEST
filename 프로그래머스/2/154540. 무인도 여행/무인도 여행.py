# 전역변수 부분이랑 
# rowCount, colCount 부분

def bfs(ci,cj):
    global v, rowCount, colCount  
    
    q = []
    q.append((ci,cj))
    count = v[ci][cj]
    v[ci][cj] = 0
    
    while q:
        ci,cj = q.pop(0)
        
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<rowCount and 0<=nj<colCount and v[ni][nj] != -1 and v[ni][nj] != 0:
                count += v[ni][nj]
                v[ni][nj] = 0
                q.append((ni,nj))
    
    return count
    

def solution(maps):
    global v, rowCount, colCount
    rowCount = len(maps)
    colCount = len(maps[0])
    answer = []
   
    v=[[0]*colCount for _ in range(rowCount)]
    
    
    for i in range(rowCount):
        for j in range(colCount):
            if maps[i][j] == "X":
                v[i][j] = -1
            else:
                v[i][j] =int(maps[i][j])
    
    
    for i in range(rowCount):
        for j in range(colCount):
            if v[i][j] != -1 and v[i][j] != 0:
                answer.append(bfs(i,j))
    
    if answer:
        return sorted(answer)
    else:
        answer.append(-1)
        return answer
    