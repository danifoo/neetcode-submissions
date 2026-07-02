class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
            
        maxLen = 1
        curLen = 1

        nums.sort()

        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                curLen += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                curLen = 1

            if curLen > maxLen:
                maxLen = curLen
        
        return maxLen