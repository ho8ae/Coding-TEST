def solution(elements):
    n = len(elements)
    answer = set()
    
    # 원형 수열을 처리하기 위해 elements를 두 번 반복
    double_elemnets = elements + elements
    
    # 각 길이의 연속 부분 수열의 합을 구함
    for i in range(1, n + 1):
        for j in range(n):
            # start부터 length 길이만큼의 합
            current_sum = sum(double_elemnets[j:j + i])
            answer.add(current_sum)
    
    return len(answer)