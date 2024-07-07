def solution(name, yearning, photo):
    answer = []
    name_score = dict(zip(name, yearning))
    
    for p in photo:
        photo_sum = 0
        for person in p:
            photo_sum += name_score.get(person, 0)
        answer.append(photo_sum)
    
    return answer
