def solution(s):
    answer = 0
    
    l = len(s)
    
    for i in range(l):
        stack = []
        valid = True
        for j in range(l):
            c = s[(i + j) % l]
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    valid = False
                    break
                if c == ')' and stack[-1] == "(":
                    stack.pop()
                elif c == ']' and stack[-1] == "[":
                    stack.pop()
                elif c == '}' and stack[-1] == "{":
                    stack.pop()
                else:
                    valid = False
                    break
        
        if valid and not stack:
            answer += 1
            
    return answer
