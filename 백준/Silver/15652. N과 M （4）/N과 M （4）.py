# 15652 N과 M (4)
# 자연수 N과 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N, M = map(int, input().split())
rs = []

def recur(num, start):  # start 매개변수 추가
    if num == M:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(start, N+1):  # start부터 시작
        rs.append(i)
        recur(num+1, i)  # 다음 숫자는 현재 숫자(i)부터 시작
        rs.pop()

recur(0, 1)