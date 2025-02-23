def solution(s):
    count = 0    # 변환 횟수
    total_zero = 0    # 전체 제거된 0의 개수
    
    while s != "1":
        # 현재 문자열의 1의 개수를 세고, 0의 개수는 전체 길이에서 빼기
        one_count = s.count("1")
        zero_count = len(s) - one_count
        total_zero += zero_count
        
        # 1의 개수를 이진수로 변환
        s = bin(one_count)[2:]
        count += 1
        
    return [count, total_zero]