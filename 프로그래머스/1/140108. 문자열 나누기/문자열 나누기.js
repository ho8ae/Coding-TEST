function solution(s) {    
    let x = null; // 첫 글자 저장
    let word = 0; // 분리된 문자열 개수
    
    // 첫 글자와 나머지 문자의 개수 카운트
    let xCnt = 0, yCnt = 0;
    
    // 문자열을 하나씩 읽음
    Array.from(s).forEach((a) => {
        if (x === null) x = a; // 첫 글자를 x로 설정
        
        if (a === x) xCnt++; // 첫 글자와 같은 문자일 경우
        else yCnt++; // 다른 문자일 경우
        
        // x와 다른 문자의 개수가 같아지면 문자열 분리
        if (xCnt === yCnt) {
            word++; // 분리된 문자열 개수 증가
            x = null; // 첫 글자 초기화
            xCnt = 0; // 카운트 초기화
            yCnt = 0; // 카운트 초기화
        }
    });
    
    // 아직 분리되지 않은 문자열이 남아있는 경우
    if (x !== null) word++;
    
    return word; // 최종 분리된 문자열 개수 반환
}