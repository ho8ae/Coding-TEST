function solution(new_id) {
    let id = new_id;
    
    // 1단계
    id = id.toLowerCase();
    
    // 2단계 - null 문제 해결
    id = id.replace(/[^a-z0-9-_.]/g, '');
    
    // 3단계
    id = id.replace(/\.+/g, '.');
    
    // 4단계
    id = id.replace(/^\.|\.$/g, '');
    
    // 5단계
    if (id.length === 0) {
        id = 'a';
    }
    
    // 6단계
    if (id.length >= 16) {
        id = id.slice(0, 15).replace(/\.$/, '');
    }
    
    // 7단계 - 현재 id를 기준으로 체크
    while (id.length <= 2) {
        id += id[id.length - 1];
    }
    
    return id;
}