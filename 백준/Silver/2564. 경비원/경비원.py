## 북을 0 으로 잡고 일직선상으로 바꿈
def cal_course(x,y):
    if x==1: # 북
        return y
    if x==2: # 남
        return W+H+(W-y)
    if x==3: # 서
        return W+H+W+(H-y)
    if x==4: # 동
        return W+y
    
W,H = map(int,input().split())
N = int(input())

course = []

for _ in range(N+1): # 0에서 상점까지 거리
    x,y=map(int,input().split())
    course.append(cal_course(x,y))

answer = 0
course

for i in range(N):
    in_course = abs(course[-1]-course[i])
    out_course = 2*(W+H) - in_course
    answer += min(in_course,out_course)


print(answer)