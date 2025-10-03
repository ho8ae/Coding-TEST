function solution(numbers, hand) {
    var answer = '';
    
    // 각 버튼의 좌표 (행, 열)
    const keypad = {
        '1': [0, 0], '2': [0, 1], '3': [0, 2],
        '4': [1, 0], '5': [1, 1], '6': [1, 2],
        '7': [2, 0], '8': [2, 1], '9': [2, 2],
        '*': [3, 0], '0': [3, 1], '#': [3, 2]
    };
    
    // 각 손의 현재 위치
    let cur_left = [3, 0];  // *
    let cur_right = [3, 2]; // #
    
    const left_keys = ['1', '4', '7'];
    const right_keys = ['3', '6', '9'];
    
    for (let num of numbers) {
        const target = num + "";
        
        // 왼쪽 열
        if (left_keys.includes(target)) {
            cur_left = keypad[target];
            answer += 'L';
        }
        // 오른쪽 열
        else if (right_keys.includes(target)) {
            cur_right = keypad[target];
            answer += 'R';
        }
        // 가운데 열 (2, 5, 8, 0)
        else {
            const target_pos = keypad[target];
            
            // 맨해튼 거리 계산
            const left_dist = Math.abs(cur_left[0] - target_pos[0]) + 
                             Math.abs(cur_left[1] - target_pos[1]);
            const right_dist = Math.abs(cur_right[0] - target_pos[0]) + 
                              Math.abs(cur_right[1] - target_pos[1]);
            
            if (left_dist < right_dist) {
                cur_left = target_pos;
                answer += 'L';
            } else if (left_dist > right_dist) {
                cur_right = target_pos;
                answer += 'R';
            } else { // 거리가 같은 경우
                if (hand === 'right') {
                    cur_right = target_pos;
                    answer += 'R';
                } else {
                    cur_left = target_pos;
                    answer += 'L';
                }
            }
        }
    }
    
    return answer;
}