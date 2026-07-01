class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFrequency = {}

        for num in nums:
            if num in numsFrequency:
                numsFrequency[num] += 1
            else:
                numsFrequency[num] = 1

        ans = []
        asc = {k: v for k, v in sorted(numsFrequency.items(), key=lambda item: item[1])}
        ans = list(asc.keys())
        ans = ans[len(ans) - k:]

        return ans
        
