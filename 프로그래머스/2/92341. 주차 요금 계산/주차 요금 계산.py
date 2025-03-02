import math

def change_records(records):
    lst = [[] for _ in range(len(records))] # [[],[],[]...[]]
    
    for i in range(len(records)):
        lst[i].append(int(records[i][:2])*60+int(records[i][3:5])) # 시간 분으로 환산하여 넣고
        lst[i].append(records[i][6:10]) # 차량 번호 넣고
        lst[i].append(records[i][11:])
    
    # print(lst)
    #[[334, 5961, 'IN'], [360, 0, 'IN'], [394, 0, 'OUT'], [479, 5961, 'OUT'], [479, 148, 'IN'], [1139, 0, 'IN'], [1149, 148, 'OUT'], [1379, 5961, 'IN'], [1380, 5961, 'OUT']]
        
    return lst
    
def solution(fees, records):
    answer = []
    # 데이터 가공
    records = change_records(records)
    
    # 번호 중복 없이 저장
    car_number = set([records[i][1] for i in range(len(records))])
    car_number = list(car_number)
    # print(car_number)  {'0148', '0000', '5961'}
    
    # 차량번호 작은 번호부터 정렬
    car_number.sort()
    
    # 요금 계산
    total = []
    for i in range(len(car_number)):
        idx= [] #records 위치 ex) 1,2
        
        
        for j in range(len(records)):
            if car_number[i] == records[j][1]:
                # 계산 j 인덱스 1,2
                idx.append(j)
    
    
        # i번째 차 계산
        #print(idx) #[1,2,5] [4,6] [0,3,7,8]
        # 길이가 알 맞을 때
        if len(idx) % 2 == 0:
            total_time = 0
            for i in range(0,len(idx),2):
                in_time = records[idx[i]][0] 
                out_time = records[idx[i+1]][0]
                total_time += out_time-in_time
            
            if total_time < fees[0]:
                answer.append(fees[1])
            else:
                additional_fee = math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
                answer.append(fees[1] + additional_fee)
        # 길이가 안 맞을때
        else:
            total_time = 0
            idx.append(-1)
            for i in range(0,len(idx),2):
                if idx[i+1] == -1:
                    out_time = (23*60)+59
                    in_time = records[idx[i]][0] 
                    total_time += out_time-in_time
                else:
                    in_time = records[idx[i]][0] 
                    out_time = records[idx[i+1]][0]
                    total_time += out_time-in_time
                    
            if total_time < fees[0]:
                answer.append(fees[1])
            else:
                additional_fee = math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
                answer.append(fees[1] + additional_fee)
            
        
        
#         # idx len(2) 인 경우
#         if len(idx) == 2:
#             in_time = records[idx[0]][0] 
#             out_time = records[idx[1]][0]
#             total_time = out_time-in_time
#             if total_time < fees[0]:
#                 answer.append(fees[1])
#             else:
#                 answer.append(fees[1]+(total_time-fees[0]/10)*600)
        
#         # 출차 기록을 23:59로 계산
#         else:
#             in_time = records[idx[0]][0] 
#             out_time = (23*60)+59
#             total_time= out_time-in_time
#             if total_time < fees[0]:
#                 answer.append(fees[1])
#             else:
#                 answer.append(fees[1]+(total_time-fees[0]/10)*600)
    
    
    return answer