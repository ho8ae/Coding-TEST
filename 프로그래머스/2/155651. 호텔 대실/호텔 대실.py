# 최소 객실의 수 BFS DFS ?
# 시간을 숫자로 바꾸기 
import heapq

def solution(book_time):
    time_lst = []
    
    # 시간 60* 으로 바꾸기
    for start, end in book_time:
        start_time = int(start[:2]) * 60 + int(start[3:])
        end_time = int(end[:2]) * 60 + int(end[3:]) + 10  # 청소 시간 10분 추가
        time_lst.append((start_time, end_time)) 
    
    time_lst.sort()
    
    rooms = []  # 현재 사용 중인 객실의 퇴실 시간을 저장할 최소 힙

    for start, end in time_lst:
        # 빈 방이 있거나 새로운 예약이 이전 예약의 퇴실+청소 시간 이후라면
        if rooms and rooms[0] <= start:
           
            # 가장 빨리 비는 방을 사용
            heapq.heappop(rooms)

        # 새 방을 추가하거나 기존 방의 퇴실 시간 업데이트
       
        heapq.heappush(rooms, end)

    
    return len(rooms)