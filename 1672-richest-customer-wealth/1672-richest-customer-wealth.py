class Solution(object):
    def maximumWealth(self, accounts):
        richest = 0
        for i in accounts:
            if richest <= sum(i):
                richest = sum(i)
        return richest