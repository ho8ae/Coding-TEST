function solution(numbers, target) {
    let count = 0;
    
    function dfs(index, total) {
        if (index === numbers.length) {
            if (total === target) {
                count++;
            }
            return;
        }
        
        dfs(index + 1, total + numbers[index]);
        dfs(index + 1, total - numbers[index]);
    }
    
    dfs(0, 0);
    return count;
}