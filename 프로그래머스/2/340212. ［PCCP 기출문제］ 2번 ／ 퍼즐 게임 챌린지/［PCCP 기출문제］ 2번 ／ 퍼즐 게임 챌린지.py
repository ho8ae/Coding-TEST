def solve(diffs_i, times_i, level_i):
    time_count = 0
    
    # diffs len만큼 반복
    for i in range(len(diffs_i)):
        if diffs_i[i] <= level_i:
            time_count += times_i[i]
        else:
            dl = diffs_i[i] - level_i
            
            # 이전 퍼즐 시간 (첫 번째 퍼즐이면 0으로 처리)
            prev_time = times_i[i-1] if i > 0 else times_i[0]
            
            # 틀릴 때마다의 시간 + 마지막 성공 시간
            time_count += (times_i[i] + prev_time) * dl + times_i[i]
            
    return time_count

def solution(diffs, times, limit):
    # 이분탐색 적용
    left = 1
    right = max(diffs)  # 최대 난이도보다 더 높은 레벨은 의미가 없음
    
    answer = right  # 최악의 경우 초기값
    
    while left <= right:
        mid = (left + right) // 2
        
        # 현재 레벨(mid)로 게임을 완료하는데 걸리는 시간
        time_needed = solve(diffs, times, mid)
        
        if time_needed <= limit:
            # 시간 내에 가능하면 레벨을 줄여봄 (최소 레벨 찾기)
            answer = mid
            right = mid - 1
        else:
            # 시간이 초과되면 레벨을 높임
            left = mid + 1
    
    return answer