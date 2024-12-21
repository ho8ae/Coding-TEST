def find_apocalypse_number(N):
    count = 0  # 찾은 종말의 수의 개수
    number = 666  # 시작 숫자
    
    while True:
        # 현재 숫자에 '666'이 포함되어 있는지 확인
        if '666' in str(number):
            count += 1
            # N번째 종말의 수를 찾았다면 반환
            if count == N:
                return number
        number += 1  # 다음 숫자로 이동

# 입력 받기
N = int(input())
# 결과 출력
print(find_apocalypse_number(N))