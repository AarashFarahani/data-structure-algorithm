from typing import Set, List

class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            self.generate(nums, i, [])

        return list(self.result)

    def generate(self, nums: List[int], index, found_list, pointer = 0):
        if pointer >= len(nums):
            self.result.append(found_list)

            if index < len(nums):
                self.generate(nums, index + 1, [])

            return []

        found_list.append(nums[pointer - index])
        return self.generate(nums, index, found_list, pointer + 1)
            

result = Solution().permute([1, 2, 3])
for item in result:
    print(item)