def solution(n):
    digits = list(str(n)) #정수 n을 문자열로 변환하고 각 자릿수를 리스트로 저장합니다.
    digits.sort(reverse = True)
    answer = int("".join(digits)) #정렬된 자릿수를 다시 하나의 문자열로 합쳐 정수로 변환
    
    return answer