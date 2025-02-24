def is_discount(dic,start,discount):
    
    want_dic = dic.copy()
    for i in range(start,start+10):
        if discount[i] in want_dic:
            want_dic[discount[i]] -= 1
    
    is_check = all(value == 0 for value in want_dic.values())
    
    return is_check

def solution(want, number, discount):
    
    answer = 0
    dis_dict = {}
    for i in range(len(want)):
        dis_dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        if is_discount(dis_dict,i,discount):
            answer += 1
    
    return answer