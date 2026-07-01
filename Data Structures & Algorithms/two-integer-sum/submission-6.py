class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  
        numsSorted = deepcopy(nums)
        numsSorted.sort()

        i = 0
        j = len(nums) - 1
        curSum = numsSorted[i] + numsSorted[j]

        for num in numsSorted:
            if(curSum == target):
                break
            elif(curSum < target):
                i += 1
                curSum = numsSorted[i] + numsSorted[j]
            elif(curSum > target):
                j -= 1
                curSum = numsSorted[i] + numsSorted[j]
        
        iAns = -1
        for k in range(0, len(nums)):
            if(nums[k] == numsSorted[i]):
                iAns = k

        jAns = -1
        for k in range(0, len(nums)):
            if(nums[k] == numsSorted[j] and k != iAns):
                jAns = k

        ans = [iAns, jAns]
        ans.sort()
        return ans