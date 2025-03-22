def solution(t, p):
    answer = 0
    psize = len(p)
    p_int = int(p)
    
    # t의 길이에서 p의 길이를 뺀 값 + 1 만큼 반복
    # (부분 문자열을 만들 수 있는 시작 위치의 개수)
    for i in range(len(t) - psize + 1):
        # i부터 i+psize까지의 부분 문자열 추출
        substring = t[i:i+psize]
        
        # 부분 문자열을 정수로 변환하여 p와 비교
        if int(substring) <= p_int:
            answer += 1
    
    return answer