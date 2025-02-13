def bfs(si,sj,fi,fj):
    # q 생성, 필요변수 생성
    q = []
    v = [0]*N
    
    # 큐에 초기데이터 삽입, si,sj는 v에  표시 x
    q.append([si,sj])
    
    while q:
        ci,cj = q.pop(0)
        if abs(ci-fi) + abs(cj-fj) <= 1000:
            return 'happy'
        
        # 미방문 모든 편의점 좌표: 범위 내 인지 체크
        for i in range(N):
            if v[i] == 0: # 미방문 편의점
                ni,nj = convi[i][0],convi[i][1]
                if abs(ni-ci) + abs(nj-cj) <= 1000:
                    q.append((ni,nj))
                    v[i] = 1
    return 'sad'
    

T=int(input())
for _ in range(T):
        
    N = int(input()) # 편의점
    si,sj = map(int,input().split())
    convi = [list(map(int,input().split())) for _ in range(N)]
    fi,fj = map(int,input().split())
    ans = bfs(si,sj,fi,fj)
    print(ans)
    