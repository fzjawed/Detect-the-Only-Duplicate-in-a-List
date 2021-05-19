class Solution:
    def solve(self, nums):
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i] == nums[j]:
                    duplicate = nums[i]
        return duplicate