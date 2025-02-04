def solution(numbers, target):
    def dfs(index, total):
        
        
        if index == len(numbers):
            return 1 if total == target else 0
        
        plus = dfs(index + 1, total + numbers[index])
        minus = dfs(index + 1, total - numbers[index])
        return plus + minus  # 여기서 결과값들이 합산됩니다!
    
    return dfs(0, 0)