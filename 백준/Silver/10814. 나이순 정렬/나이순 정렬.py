n = int(input())

g = []
for _ in range(n):
    age,name = input().split()
    g.append([int(age),name])
    
for i in sorted(g,key=lambda x: x[0]):
    print(i[0],i[1])