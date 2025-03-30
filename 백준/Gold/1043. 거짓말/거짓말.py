# 1043
N, M = map(int, input().split())
true_info = list(map(int, input().split()))
true_count = true_info[0]  # 진실을 아는 사람의 수

# 진실을 아는 사람이 없으면 모든 파티에서 거짓말 가능
if true_count == 0:
    result = M
    for _ in range(M):
        input()  # 입력 소비
    print(result)
else:
    true_people = set(true_info[1:])  # 진실을 아는 사람들 집합
    
    # 파티 정보 저장
    parties = []
    party_people = [[] for _ in range(N+1)]  # 각 사람이 참여하는 파티 번호 저장
    
    for i in range(M):
        p_lst = list(map(int, input().split()))
        party = p_lst[1:]  # 파티 참가자 목록
        parties.append(party)
        
        # 각 사람이 어떤 파티에 참여하는지 저장
        for person in party:
            party_people[person].append(i)
    
    # 진실을 알게 되는 사람들 전파 (BFS 방식으로 변경)
    queue = list(true_people)
    known_parties = set()  # 진실을 말해야 하는 파티
    
    while queue:
        person = queue.pop(0)
        
        # 이 사람이 참여하는 모든 파티 확인
        for party_idx in party_people[person]:
            if party_idx not in known_parties:
                known_parties.add(party_idx)
                
                # 이 파티의 모든 사람도 진실을 알게 됨
                for new_person in parties[party_idx]:
                    if new_person not in true_people:
                        true_people.add(new_person)
                        queue.append(new_person)
    
    # 거짓말할 수 있는 파티의 수
    result = M - len(known_parties)
    print(result)