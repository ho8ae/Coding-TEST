#17219

n,m = map(int,input().split())
add={}
for _ in range(n):
    x,y = input().split()
    add[x]=y
for _ in range(m):
    print(add[input()])