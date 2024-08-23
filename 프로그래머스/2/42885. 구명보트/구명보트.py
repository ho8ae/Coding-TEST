def solution(people, limit):
    
    people.sort()
    count = 0
    
    i =0 #가벼운 사람
    j = len(people) -1 #가장 무거운 사람
    
    while i <= j:
        if people[i] +people[j] <= limit:
            i += 1
        #무거운 사람만 태울 수 있으면 무거운 사람만 보냄
        j-=1
        count +=1 
    return count
    