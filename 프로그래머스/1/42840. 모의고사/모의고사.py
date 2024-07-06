def solution(answers):
    pat1 = [1, 2, 3, 4, 5]
    pat2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == pat1[idx % len(pat1)]:
            scores[0] += 1
        if answer == pat2[idx % len(pat2)]:
            scores[1] += 1
        if answer == pat3[idx % len(pat3)]:
            scores[2] += 1
    
    max_score = max(scores)
    
    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i + 1)
    
    return result
