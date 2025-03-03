#A : 65 Z : 89
#	{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
def solution(msg):
    answer = []
    dic ={}
    
    for idx,i in enumerate(range(65,91)):
        dic[chr(i)] = idx+1
        
    while True:
        # 해당 글자가 사전에 있다면
        if msg in dic:
            answer.append(dic[msg])
            break
            
        for i in range(1,len(msg)):
            # 다음 글자가 포함하지 않느다면
            if msg[:i+1] not in dic:
                answer.append(dic[msg[:i]])
                dic[msg[:i+1]] = len(dic)+1
                msg = msg[i:]
                break
    
    return answer