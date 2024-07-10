def solution(num_list):
    answer=0
    answer1= 1
    answer2= 0
    
    for num in num_list:
        answer1 *= num
        answer2 += num
    
    answer_squere = answer2*answer2
    
    if answer1 < answer_squere:
        answer=1
    else:
        answer=0
    
    return answer