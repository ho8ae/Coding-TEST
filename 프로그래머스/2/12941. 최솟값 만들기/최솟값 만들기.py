def solution(A,B):
    
    Alst = sorted(A)
    Blst = sorted(B, reverse=True)
    total = 0
    for i in range(len(Alst)):
        total += Alst[i]*Blst[i]

    return total