# 랭킹 대기전

p,m = map(int,input().split())
rooms = [] # [방의 기준 레벨, [[레벨,닉네임],[레벨,닉네임]...]?..

for _ in range(p):
    level,nick = input().split()
    level =int(level)
    is_assigned = False # 방 가능 한지?
    
    # 1. 들어갈 수 있는 방이 있는지 확인
    
    for room in rooms:
        standard_level = int(room[0]) # 방의 기준 레벨
        # 레벨 조건 확인 및 방이 꽉 차지 않았는지 확인
        if standard_level -10 <= level <= standard_level+10 and len(room[1]) < m:
            room[1].append([level,nick])
            is_assigned = True
            break
    
    # 2. 방이 없다면 새로운 방 생성
    if not is_assigned:
        rooms.append([level,[[level,nick]]])
        
for room in rooms:
    players = sorted(room[1], key= lambda x:x[1])
    
    #방의 상태 출력(Started! or Waiting!)
    if len(players) == m:
        print("Started!")
    else:
        print("Waiting!")
        
    # 방에 있는 플레이어 출력
    
    for level,nick in players:
        print(level,nick)
        
        