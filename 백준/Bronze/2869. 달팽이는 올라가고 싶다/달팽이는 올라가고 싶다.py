A, B, V = map(int, input().split())

x = (V-B)/(A-B) #방정식 만들어서 식을 풀어냄
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)