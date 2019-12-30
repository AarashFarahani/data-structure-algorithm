from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.permute([], nums)
		
    def permute(self, trace: List[int], nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [trace + nums]
        results = []
        appeared = set()
        for i, n in enumerate(nums):
            if n not in appeared:
                # skip duplicates
                results += self.permute(trace + [n], nums[:i] + nums[i+1:])
                appeared.add(nums[i])
        return results

result = Solution().permuteUnique([1, 1, 2])
for item in result:
    print(item)