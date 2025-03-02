def is_able(l,s): #['C','B','D'],"BACDE"
    # BACDE visited 만들기
    arr = list(s) # ['B','A','C','D','E']
    stack = []
    
    for i in range(len(arr)):
        if arr[i] in l:
            stack.append(arr[i])
    

    
    if l[:len(stack)] == stack:
        return True
    else:
        return False
    

def solution(skill, skill_trees):
    answer = 0
    # skil list로
    lst = list(skill)
    
    for skill_tree in skill_trees:
        if is_able(lst,skill_tree):
            answer += 1 
    
    
    
    return answer