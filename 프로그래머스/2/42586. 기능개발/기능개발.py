def clac(p,s):
    count = 0
    
    while p<100:
        p+=s
        count+=1
    return count

def solution(progresses, speeds):
    
    reply = []
    answer = []
    for j in range(len(progresses)):
        reply.append(clac(progresses[j],speeds[j]))
    
    left = 0
  

    while left < len(reply):
        dekiru = 1
        right = left + 1 
        
       
        while right < len(reply) and reply[left] >= reply[right]:
            right += 1
            dekiru += 1
        
        answer.append(dekiru)
        left = right  #
    
    return answer