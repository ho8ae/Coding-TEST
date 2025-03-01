from itertools import permutations
import math

def is_primer(num):
    
    if num == 1 or num == 0:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num % i ==0:
            return False
    return True

def solution(numbers):
    arr= []
    lst = []
    
    answer = 0
    
    for num in numbers:
        arr.append(int(num))
    
    for r in range(1,len(arr)+1):
        for node in permutations(arr,r):
            lst.append(node)
        
    nset = set(lst)
    lst = []
    for node in nset:
        
        # 문자열로
        map_s = ''.join(str(digit) for digit in node)
        
        # 다시 정수로
        map_s = int(map_s)
        
        # 리스트로
        lst.append(map_s)
    lst = set(lst)
    for num in lst:
        if is_primer(num):
            answer +=1
    
    
    return answer