def solution(s):
    # 스택과 큐를 이용하자
    arr = []
    for c in s:
        if c not in arr:
            arr.append(c)
        else:
            if arr[-1] == c:
                arr.pop()
            else:
                arr.append(c)
    
    if len(arr) == 0:
        return 1
    else:
        return 0
    
    