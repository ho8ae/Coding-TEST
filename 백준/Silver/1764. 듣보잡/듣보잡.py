# 1764 듣보잡

n,m = map(int,input().split())

listen = []
see = []

for _ in range(n):
    listen.append(input())

for _ in range(m):
    see.append(input())
    
# see = [a,b,c]
# listen = [a,b]

# 출력 [a,b]
# 교집합을 찾자

result = sorted(list(set(listen) &set(see)))

print(len(result))
for name in result:
    print(name)
