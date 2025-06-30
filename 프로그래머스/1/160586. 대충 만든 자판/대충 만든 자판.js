// 두 키맵 중 제일 적은 거 추합

function solution(keymap, targets) {
    let answer = []
    let temp;
  for(let target of targets){
      let sum = 0
      for(let i =0; i<target.length; i++){
          let mn=101;
          
          for(let key of keymap){
              for(let j = 0; j<key.length; j++){
                 if(key[j]==target[i]){
                   if(mn > j+1){
                       mn = j+1
                   }
                   break;
                }
              }
          }
           if(mn === 101){
              sum = -1;
              break;
          }
          sum += mn
          
          
      }
      if(sum === -1 ){
              answer.push(-1);
             
          }
      else{
          answer.push(sum)}
      sum = 0
  }
   
    
   return answer;
}