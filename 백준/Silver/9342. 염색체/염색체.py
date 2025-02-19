# 9342 염색체
import re

p = re.compile('[A-F]?A+F+C+[A-F]?')
T = int(input())
for _ in range(T):
    chars = input()
    if p.fullmatch(chars):
        print('Infected!')
    else:
        print('Good')