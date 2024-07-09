def solution(s):
    
    stack=list()
    
    for c in s:
        if c=='(':
            stack.append(c)
        if c==')':
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack)==0
        

    return True