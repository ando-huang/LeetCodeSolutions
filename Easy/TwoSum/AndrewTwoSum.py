'''
    62ms, beats 75.91%
    17.7MB, beasts 17.16%
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return [num_dict[target-nums[i]], i]
            num_dict[nums[i]] = i
