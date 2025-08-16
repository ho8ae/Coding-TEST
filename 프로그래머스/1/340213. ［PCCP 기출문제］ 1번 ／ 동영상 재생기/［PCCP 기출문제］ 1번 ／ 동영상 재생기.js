function solution(video_len, pos, op_start, op_end, commands) {
    var answer = '';
    
    // 전부 sec으로 변환
    let all = [video_len,pos,op_start,op_end];
    for(let i =0; i<all.length; i++){
        let [m,s] = all[i].split(":")
        all[i]  = Number(m)*60+Number(s)
    }
    let [v,p,os,oe] = all
    console.log(v,p,os,oe)
    for(let i=0; i<commands.length; i++){
        // 현재 재생 위치가 오프닝 구간인지 확인
        // op 사이라면
        if(p >= os && p <= oe){
            p = oe;
        }
        
        if(commands[i] === 'next'){
            p += 10;
        
            if(p>v){
                p=v
            }
            
            // op 사이라면
            if(p >= os && p <= oe){
                p = oe;
            }
        }else if(commands[i] === 'prev'){
            p -= 10;    
            // minus 나온다면 0으로 만들기
            if(p < 0){
                p = 0
            }
            
            // op 사이라면
            if(p >= os && p <= oe){
                p = oe;
            }
        }
        
    }
    
    
     console.log("p 끝난 후 ",p)
    // p 변환
    let m = Math.floor(p/60);
    let s = Math.floor(p%60);
    
    if(m<10) m = '0'+m
    if(s<10) s = '0'+s
    
    return `${m}:${s}`
    
   
}
    