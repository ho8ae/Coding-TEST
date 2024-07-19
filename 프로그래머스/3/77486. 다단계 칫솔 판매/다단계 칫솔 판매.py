def solution(enroll, referral, seller, amount):
    #parent 딕셔너리 key는 enroll의 노드,value는 referral의 노드로 구성됨
    #(enroll의 부모노드) ->referral이 됨 따라서 키 값으로 벨류를 찾는거임
    parent= dict(zip(enroll,referral))
    
    #total 딕셔너리 생성 및 초기화
    total ={name:0 for name in enroll}
    
    #seller 리스트와 amount 리스트를 이용하여 이익 분배
    for i in range(len(seller)):
        #판매자가 판매한 총 금액 계산
        money = amount[i]*100
        cur_name = seller[i]
        #판매자로부터 차례대로 사위 노드로 이동하여 이익 분배
        while money > 0 and cur_name!='-':
            total[cur_name] += money-money//10
            cur_name = parent[cur_name] #여기서 cur_name을 부모 노드로 바꿔줌
            #10%를 제외한 금액을 계산
            money//=10
    
    return [total[name] for name in enroll]