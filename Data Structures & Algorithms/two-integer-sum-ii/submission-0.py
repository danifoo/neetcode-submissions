class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while(l < len(numbers) - 1 and r > 0):
            cur_sum = numbers[l] + numbers[r]
            if(cur_sum == target):
                break
            elif(target > cur_sum):
                l += 1
            else:
                r -= 1

        return [l + 1, r + 1]


        

         