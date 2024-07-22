def solution(players, callings):
    # 각 플레이어의 위치를 저장하는 딕셔너리
    player_positions = {player: i for i, player in enumerate(players)}
    
    for c in callings:
        # 호출된 플레이어의 현재 위치
        current_pos = player_positions[c]
        
        # 첫 번째 플레이어가 아닌 경우에만 자리를 바꿈
        if current_pos > 0:
            # 앞에 있는 플레이어
            player_to_swap = players[current_pos - 1]
            
            # 플레이어 리스트에서 자리 바꿈
            players[current_pos], players[current_pos - 1] = players[current_pos - 1], players[current_pos]
            
            # 딕셔너리에서 위치 업데이트
            player_positions[c] -= 1
            player_positions[player_to_swap] += 1
    
    return players
