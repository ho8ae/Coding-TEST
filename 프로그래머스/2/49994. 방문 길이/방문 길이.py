def solution(dirs):
    s=set() # 내가 갔던 좌표 다 저장하면 될 것 같은데 현재좌표 다음좌표 & 다음좌표 내가 간 좌표 중복X
    d = {'U':(-1,0),
        'D':(1,0),
        'R':(0,1),
        'L':(0,-1)
        }
    x,y = 0,0
    
    for dir in dirs:
        nx,ny=  x+d[dir][0],y+d[dir][1]
        if -5<=nx<=5 and -5<=ny<=5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x,y=nx,ny
    
    return len(s)//2