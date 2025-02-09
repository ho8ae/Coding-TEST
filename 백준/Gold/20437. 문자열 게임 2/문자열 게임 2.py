def solve(W, K):
    if K > len(W):  # K가 문자열 길이보다 크면 불가능
        return [-1]
        
    min_length = float('inf')  # 가장 짧은 길이
    max_length = -1  # 가장 긴 길이
    
    # 각 알파벳의 위치를 저장
    char_positions = {}
    for i, char in enumerate(W):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)
    
    # 각 문자에 대해 K개를 포함하는 연속 문자열 찾기
    for char, positions in char_positions.items():
        if len(positions) >= K:  # K개 이상 있는 문자에 대해서만
            # K개씩 묶어서 확인
            for i in range(len(positions) - K + 1):
                # 현재 위치부터 K개 뒤의 위치까지의 길이
                curr_length = positions[i + K - 1] - positions[i] + 1
                
                # 첫글자와 마지막 글자가 같은 경우(항상 같음)
                if K == 1 or (positions[i] == 0 or W[positions[i]] == W[positions[i + K - 1]]):
                    max_length = max(max_length, curr_length)
                
                min_length = min(min_length, curr_length)
    
    if min_length == float('inf'):  # 가능한 경우가 없으면
        return [-1]
    
    return [min_length, max_length]

# 입력 처리
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    result = solve(W, K)
    if len(result) == 1:
        print(-1)
    else:
        print(result[0], result[1])