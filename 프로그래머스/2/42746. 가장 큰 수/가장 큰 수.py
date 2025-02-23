def solution(numbers):
    numbers = list(map(str,numbers))
    answer =''
    lst = sorted(numbers,key=lambda x: x*3,reverse=True)

    for i in lst:
        answer += i

    
    return str(int(answer))