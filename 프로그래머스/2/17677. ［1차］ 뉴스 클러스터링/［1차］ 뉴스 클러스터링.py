import math

def make_lst(str):
    result = []
    str = str.lower()
    
    for i in range(len(str) - 1):
        # 두 글자가 모두 알파벳인 경우만 추가
        if 'a' <= str[i] <= 'z' and 'a' <= str[i+1] <= 'z':
            result.append(str[i] + str[i+1])
    
    return result

def solution(str1, str2):
    str1_lst = make_lst(str1)
    str2_lst = make_lst(str2)
    
    # 둘다 공집합이라면
    if not str1_lst and not str2_lst:
        return 65536
    
    # 다중집합 처리를 위한 딕셔너리
    str1_dict = {}
    str2_dict = {}
    
    # 원소 개수 세기
    for elem in str1_lst:
        if elem in str1_dict:
            str1_dict[elem] += 1
        else:
            str1_dict[elem] = 1
    
    for elem in str2_lst:
        if elem in str2_dict:
            str2_dict[elem] += 1
        else:
            str2_dict[elem] = 1
    
    # 교집합과 합집합 크기 계산
    intersection_size = 0
    union_size = 0
    
    # 모든 고유 원소 수집
    all_elements = set(str1_dict.keys()) | set(str2_dict.keys())
    
    print(str2_dict.get('aa',0))
    
    
    for elem in all_elements:
        # 교집합: 각 원소의 최소 개수
        count1 = str1_dict.get(elem, 0)
        count2 = str2_dict.get(elem, 0)
        intersection_size += min(count1, count2)
        
        # 합집합: 각 원소의 최대 개수
        union_size += max(count1, count2)
    
    # 자카드 유사도 계산
    similarity = intersection_size / union_size if union_size > 0 else 1
    
    return math.floor(similarity * 65536)