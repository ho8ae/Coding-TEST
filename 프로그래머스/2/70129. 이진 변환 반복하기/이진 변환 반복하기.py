import re
def solution(s):
    
    count = 0
    zero_count=0
    while len(s) != 1:
        zero_count += s.count('0')
        s=re.sub(r'[^1]','',s)
        s=bin(len(s))[2:]
        count += 1
    
    answer=[count,zero_count]
        
    return answer