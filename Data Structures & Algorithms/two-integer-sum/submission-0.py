class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique_dict = {}
        for pos in range(len(nums)):
            complement = target - nums[pos]
            if complement in unique_dict:
                return [unique_dict[complement], pos]
            unique_dict[nums[pos]] = pos
