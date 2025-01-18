N = int(input())
coordinate = list(map(int, input().split()))
result = []

def coordinateCount(coordinate):
    # 중복 제거하고 정렬한 리스트 생성
    unique_coords = sorted(list(set(coordinate)))
    
    # 딕셔너리를 사용하여 값과 인덱스 매핑
    coord_dict = {value: index for index, value in enumerate(unique_coords)}
    
    # 원본 좌표를 압축된 좌표로 변환
    for num in coordinate:
        result.append(coord_dict[num])
        
    return print(*result)

coordinateCount(coordinate)