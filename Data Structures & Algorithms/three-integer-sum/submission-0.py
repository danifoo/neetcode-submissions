class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()
        for i in range(0, len(nums)):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1

            target = -nums[i]
            while (l < r):
                curSum = nums[l] + nums[r]
                if(curSum > target):
                    r -= 1
                elif(curSum < target):
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res 

