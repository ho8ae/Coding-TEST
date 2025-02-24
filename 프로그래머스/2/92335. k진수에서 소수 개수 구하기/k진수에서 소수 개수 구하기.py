import math

def is_prime_number(x):
    # 빈 문자열이거나 1 이하인 경우 처리
    if x == '' or x == '1' or int(x) < 2:
        return False
    
    # 문자열을 정수로 변환
    x = int(x)
    
    # 소수 판별 (sqrt(x) + 1까지 검사)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def make_k(n,q):
    
    rev_base = ''
    
    while n>0:
        n,mod = divmod(n,q)
        rev_base += str(mod)
    
    return rev_base[::-1]
    
def solution(n, k):
    count = 0
    
    # [1] n을 k진수로 변경
    k_lst = make_k(n, k)
    
    # [2] 0에 따라서 리스트에 담는다
    k_lst = k_lst.split("0")
    
    # [3] 각 숫자가 소수인지 확인
    for num in k_lst:
        if is_prime_number(num):
            count += 1
    
    return count