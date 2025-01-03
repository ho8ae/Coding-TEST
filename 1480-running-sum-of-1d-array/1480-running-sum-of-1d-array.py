class Solution(object):
    def runningSum(self, nums):
        for i in range(len(nums)):
            if i == 0: continue
            else:
                nums[i] += nums[i-1]
        return nums