function solution(today, terms, privacies) {
  let answer = [];
  
  // 1. 약관 딕셔너리 생성
  let termMap = {};
  terms.forEach(t => {
    let [type, months] = t.split(' ');
    termMap[type] = Number(months);
  });

  // 2. 날짜 → 총 일수 변환 함수
  function toDays(dateStr) {
    let [y, m, d] = dateStr.split('.').map(Number);
    return y * 12 * 28 + m * 28 + d;
  }

  // 3. 오늘 날짜 일수
  let todayDays = toDays(today);

  // 4. 개인정보별 만료일 계산
  privacies.forEach((p, idx) => {
    let [date, type] = p.split(' ');
    let expireDays = toDays(date) + termMap[type] * 28 - 1;
    if (expireDays < todayDays) {
      answer.push(idx + 1);
    }
  });

  return answer;
}
