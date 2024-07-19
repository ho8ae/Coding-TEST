def solution(phone_book):
    
    phone_dic = {}
    for p in phone_book:
        phone_dic[p]=1
    
    for p in phone_book:
        temp =''
        
        for c in p:
            temp+=c
            if temp in phone_dic and temp != p :
                return False
    return True
    