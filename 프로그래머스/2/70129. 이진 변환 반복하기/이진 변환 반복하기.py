def solution(s):
    
    #이진 변환 횟수를 저장하는 변수
    count_transform = 0
    #제거된 모든 0의 개수를 저장하는 변수
    count_zero = 0
    
    while s!="1":
        count_transform +=1
        
        count_zero += s.count("0")
        s=bin(s.count("1"))[2:]
        
    return [count_transform,count_zero]