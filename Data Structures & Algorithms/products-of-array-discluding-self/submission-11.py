class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeroCounter = 0
        allProducts = 1

        for num in nums:
            if num != 0:
                allProducts *= num
            else:
                zeroCounter += 1
        
        ans = []
        if zeroCounter >= 2:
            return [0] * len(nums)
        elif zeroCounter == 1:
            for num in nums:
                if num != 0:
                    ans.append(0)
                else: 
                    ans.append(allProducts)
        else:
            for num in nums:
                ans.append(int(allProducts/num))
            

        return ans
            
