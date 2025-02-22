# 12933 오리 

S = input() # quqacukqauackck
char = ['q','u','a','c','k']
quackCount = 0 # 그냥 0 으로 시작
v = [0]*len(S)
num = 0

if S[0] != 'q' or len(S) % 5 != 0:
    print(-1)
else:
    while num < len(S) :
        d = 0
        found = False # 오리 찾았는지 체크용
        for i in range(len(S)):
            if S[i] == char[d] and v[i] == 0: # 현재 스펠 같으면
                d += 1
                num += 1
                v[i] = 1
                if d == 5:
                    found = True
                    d = 0 #다시 처음부터
                    
        if found: # 오리 찾은 경우
            quackCount += 1
        elif num < len(S): # 못 찾았는데 아직 처리 할 문자가 남은 경우
            print(-1)
            exit()

    if 0 in v:
        print(-1)
    else:
        print(quackCount)
    