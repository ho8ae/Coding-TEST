#2475

num = map(int, input().split())

result = 0

num

for i in num:
    result += i ** 2

print(result%10)