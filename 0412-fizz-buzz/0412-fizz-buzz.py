class Solution(object):
    def fizzBuzz(self, n):
        grid = []
        for i in range(1, n+1):  # 1부터 n까지
            if i % 3 == 0 and i % 5 == 0:
                grid.append("FizzBuzz")
            elif i % 3 == 0:
                grid.append("Fizz")
            elif i % 5 == 0:
                grid.append("Buzz")
            else:
                grid.append(str(i))
        return grid
        